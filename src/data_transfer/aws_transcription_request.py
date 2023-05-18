from dataclasses import dataclass

from data_transfer.transcription_request import TranscriptionRequest


@dataclass(frozen=True)
class AwsTranscriptionRequest(TranscriptionRequest):
    output_bucket_name: str
    output_key: str