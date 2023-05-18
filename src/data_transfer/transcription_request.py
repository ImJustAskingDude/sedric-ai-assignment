from dataclasses import dataclass


@dataclass(frozen=True)
class TranscriptionRequest:
    job_name: str
    language_code: str
    media_format: str
    media_file_uri: str