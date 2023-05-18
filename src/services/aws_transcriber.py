import boto3
from data_transfer.aws_transcription_request import AwsTranscriptionRequest
from domain.models.transcription import Transcription

from services.interfaces.transcriber import Transcriber


class AwsTranscriber(Transcriber):
    def __init__(self) -> None:
        self._client = boto3.client("transcribe")

    def transcribe(self, transcription_request: AwsTranscriptionRequest):
        response = self._client.start_transcription_job(
            TranscriptionJobName=transcription_request.job_name,
            LanguageCode=transcription_request.language_code,
            MediaFormat=transcription_request.media_format,
            Media={"MediaFileUri": transcription_request.media_file_uri},
            OutputBucketName=transcription_request.output_bucket_name,
            OutputKey=transcription_request.output_key,
        )

        return response
