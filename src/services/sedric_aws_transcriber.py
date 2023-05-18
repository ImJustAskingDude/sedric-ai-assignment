from data_transfer.aws_transcription_request import AwsTranscriptionRequest
from services.aws_transcriber import AwsTranscriber


class SedricAwsTranscriber:
    def __init__(self, aws_transcriber: AwsTranscriber) -> None:
        self._aws_transcriber = aws_transcriber

    def transcribe(self, transcription_request: AwsTranscriptionRequest):
        return self._aws_transcriber.transcribe(
            transcription_request=transcription_request,
            output_bucket_name="sedric-transcription-results",
            output_key=f"{transcription_request.job_name}.json",
        )
