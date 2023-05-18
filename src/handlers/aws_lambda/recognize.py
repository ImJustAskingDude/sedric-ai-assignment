import jsons

from uuid import uuid4

from data_transfer.aws_event import AwsEvent
from data_transfer.recognize_request import RecognizeRequest
from data_transfer.recognize_response import RecognizeResponse
from data_transfer.recognize_response_body import RecognizeResponseBody
from data_transfer.transcription_request import TranscriptionRequest
from domain.models.s3_media_file_uri import S3MediaFileUri
from domain.models.sedric_transcription import SedricTranscription
from services.sedric_aws_transcriber import SedricAwsTranscriber


def handle(event: dict, context):
    print(event)
    aws_event = jsons.load(json_obj=event, cls=AwsEvent)
    aws_event_body = aws_event.body

    if aws_event_body == None or aws_event_body.replace(" ", "") == "":
        return {
            "isBase64Encoded": False,
            "statusCode": 400,
            "headers": {"Content-Type": "application/json"},
            "body": jsons.dumps("You have not provided the body for the POST request."),
        }

    request = jsons.loads(aws_event_body, RecognizeRequest)
    print(request)

    bucket_name = "sedric-transcription-audio"

    s3_media_file_uri = S3MediaFileUri(
        bucket_name=bucket_name, file_name="still-listening-gentleman.wav"
    )

    request_id = str(uuid4())

    transcription = SedricTranscription(
        job_name=str(request_id), s3_media_file_uri=s3_media_file_uri
    )

    transcription_request = TranscriptionRequest.from_transcription(
        transcription=transcription
    )

    transcription_service = SedricAwsTranscriber()
    transcription_response = transcription_service.transcribe(
        transcription_request=transcription_request
    )

    print(f"{transcription_response=}")

    response = RecognizeResponse(
        body=RecognizeResponseBody(
            request_id=request_id,
            message="Your request was accepted successfully",
        )
    )

    return {
        "isBase64Encoded": False,
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": jsons.dumps(response),
    }
