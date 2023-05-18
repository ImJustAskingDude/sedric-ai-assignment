from data_transfer.transcription_request import TranscriptionRequest
from services.aws_transcriber import AwsTranscriber
from services.interfaces.transcriber import Transcriber


class SedricAwsTranscriber(Transcriber):
    def __init__(self, aws_transcriber: AwsTranscriber) -> None:
        self._aws_transcriber = aws_transcriber

    def transcribe(self, transcription_request: TranscriptionRequest):
        return self._aws_transcriber.transcribe(
            transcription_request=transcription_request,
            output_bucket_name="sedric-transcription-results",
            output_key=f"{transcription_request.job_name}.json",
        )
