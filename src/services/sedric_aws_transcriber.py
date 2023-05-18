from data_transfer.aws_transcription_request import AwsTranscriptionRequest
from data_transfer.transcription_request import TranscriptionRequest
from services.aws_transcriber import AwsTranscriber
from services.interfaces.transcriber import Transcriber


class SedricAwsTranscriber(Transcriber):
    def __init__(self, aws_transcriber: AwsTranscriber) -> None:
        self._aws_transcriber = aws_transcriber

    def transcribe(self, transcription_request: TranscriptionRequest):
        aws_transcription_request = AwsTranscriptionRequest(
            job_name=transcription_request.job_name,
            language_code=transcription_request.language_code,
            media_format=transcription_request.media_format,
            media_file_uri=transcription_request.media_file_uri,
            output_bucket_name="sedric-transcription-results",
            output_key=f"{transcription_request.job_name}.json",
        )

        return self._aws_transcriber.transcribe(
            transcription_request=aws_transcription_request,
        )
