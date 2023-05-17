import boto3
from src.domain.models.transcription import Transcription

from src.services.interfaces.transcriber import Transcriber


class AwsTranscriber(Transcriber):
    def __init__(self) -> None:
        self._client = boto3.client("transcribe")

    def transcribe(self, transcription: Transcription):
        response = self._client.start_transcription_job(
            TranscriptionJobName=transcription._job_name,
            LanguageCode=transcription._language_code.value,
            MediaFormat=transcription._media_format.value,
            Media={"MediaFileUri": transcription._media_file_uri.get_file_name()},
        )

        return response
