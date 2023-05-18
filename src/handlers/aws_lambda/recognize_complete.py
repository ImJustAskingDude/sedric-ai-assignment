# import jsons

# from data_transfer.aws_event import AwsEvent
# from data_transfer.recognize_request import RecognizeRequest
# from data_transfer.recognize_response import RecognizeResponse
# from data_transfer.recognize_response_body import RecognizeResponseBody
# from domain.models.s3_media_file_uri import S3MediaFileUri
# from domain.models.sedric_transcription import SedricTranscription
# from services.aws_transcriber import AwsTranscriber


# def handle(event: dict, context):
# import json
# import boto3
# import urllib.request

import dataclasses
from os import path
from uuid import uuid4
import jsons
import boto3
from data_transfer.aws_dynamodb_recognize_request import AwsDynamoDbRecognizeRequest

from data_transfer.aws_event_sns import AwsEventSns
from data_transfer.aws_sns_s3_message import AwsSnsS3Message
from data_transfer.recognize_result import RecognitionResult
from data_transfer.recognize_result_sentence import RecognitionResultSentence
from services.sedric_aws_s3 import SedricAwsS3
from services.sedric_sentence_finder import SedricSentenceFinder
from utils.collection_utils import get_first

# Create the DynamoDB client
# dynamodb = boto3.resource('dynamodb')
# table = dynamodb.Table('RecognitionResults')

sedric_aws_s3 = SedricAwsS3()

dynamodb = boto3.resource("dynamodb")

requests_table_name = "sedric-transcription-requests"
requests_table = dynamodb.Table(requests_table_name)

results_table_name = "sedric-transcription-results"
results_table = dynamodb.Table(results_table_name)


def handle(event, context):
    print(event)

    aws_event = jsons.load(event, AwsEventSns)
    aws_event_first_record = get_first(aws_event.Records)
    aws_event_message = aws_event_first_record.Sns.Message

    aws_s3_message = jsons.loads(aws_event_message, AwsSnsS3Message)

    recognize_first_result = get_first(aws_s3_message.Records)
    recognize_result_file_name = recognize_first_result.s3.object.key

    if ".write_access_check_file.temp" in recognize_result_file_name:
        return {
            "isBase64Encoded": False,
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": jsons.dumps(event),
        }

    request_id = path.splitext(recognize_result_file_name)[0]
    transcription_response = sedric_aws_s3.get_transcription(request_id=request_id)

    transcription_results = transcription_response.results
    transcription_transcript = get_first(transcription_results.transcripts)
    transcription_text = transcription_transcript.transcript

    key = {
        'requestId': request_id
    }

    request_item = requests_table.get_item(Key=key)['Item']
    print(request_item)
    recognize_request = jsons.load(request_item, AwsDynamoDbRecognizeRequest)

    sentence_finder = SedricSentenceFinder()
    sentence_keys_per_sentence = sentence_finder.find(
        transcription_text=transcription_text, sentences=recognize_request.sentences
    )

    recognize_result_sentences = [
        RecognitionResultSentence(
            plain_text=sentence,
            was_present=len(sentence_keys) != 0,
            start_word_index=sentence_key.get_start_index()
            if len(sentence_keys) != 0
            else None,
            end_word_index=sentence_key.get_end_index()
            if len(sentence_keys) != 0
            else None,
        )
        for sentence, sentence_keys in sentence_keys_per_sentence.items()
        for sentence_key in sentence_keys
    ]

    audio_url = recognize_request.audioFileUrl

    recognize_results = RecognitionResult(
        resultId=str(uuid4()),
        requestId=request_id,
        audioUrl=audio_url,
        transcriptionUrl=None,
        sentences=recognize_result_sentences,
    )

    item = dataclasses.asdict(recognize_results)

    print(f"Putting {item=} in table {results_table_name}")
    results_table.put_item(Item=item)

    return {
        "isBase64Encoded": False,
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": jsons.dumps(event),
    }
