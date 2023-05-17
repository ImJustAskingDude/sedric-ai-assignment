import jsons

from data_transfer.aws_event import AwsEvent
from data_transfer.recognize_request import RecognizeRequest
from data_transfer.recognize_response import RecognizeResponse
from data_transfer.recognize_response_body import RecognizeResponseBody
from domain.models.s3_media_file_uri import S3MediaFileUri
from domain.models.sedric_transcription import SedricTranscription
from services.aws_transcriber import AwsTranscriber


def handle(event: dict, context):
    print(event)
    aws_event = jsons.load(json_obj=event, cls=AwsEvent)
    aws_event_body = aws_event.body

    request = jsons.loads(aws_event_body, RecognizeRequest)
    print(request)

    bucket_name = "sedric-transcription-audio"

    s3_media_file_uri = S3MediaFileUri(
        bucket_name=bucket_name, file_name="still-listening-gentleman.wav"
    )

    transcription = SedricTranscription(
        job_name="sample_transcription_job", s3_media_file_uri=s3_media_file_uri
    )

    transcription_service = AwsTranscriber()
    transcription_response = transcription_service.transcribe(
        transcription=transcription
    )

    print(f"{transcription_response=}")

    response = RecognizeResponse(
        body=RecognizeResponseBody(
            request_id="generated_request_id",
            message="Your request was accepted successfully",
        )
    )

    return {
        "isBase64Encoded": False,
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": jsons.dumps(response),
    }
