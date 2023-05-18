import boto3
from domain.models.transcription import Transcription

from services.interfaces.transcriber import Transcriber


class AwsTranscriber(Transcriber):
    def __init__(self) -> None:
        self._client = boto3.client("transcribe")

    def transcribe(self, transcription: Transcription, output_bucket_name: str, output_key: str):
        response = self._client.start_transcription_job(
            TranscriptionJobName=transcription._job_name,
            LanguageCode=transcription._language_code.value,
            MediaFormat=transcription._media_format.value,
            Media={"MediaFileUri": transcription._media_file_uri.get_file_name()},
            OutputBucketName=output_bucket_name,
            OutputKey=output_key,
        )

        return response
