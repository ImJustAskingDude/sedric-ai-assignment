from dataclasses import dataclass

from domain.models.transcription import Transcription


@dataclass(frozen=True)
class TranscriptionRequest:
    job_name: str
    language_code: str
    media_format: str
    media_file_uri: str

    @classmethod
    def from_transcription(cls: 'TranscriptionRequest', transcription: Transcription) -> 'TranscriptionRequest':
        return TranscriptionRequest(
            job_name=transcription.get_job_name(),
            language_code=transcription.get_language_code().value,
            media_format=transcription.get_media_format().value,
            media_file_uri=transcription.get_media_file_uri().get_file_name()
        )