from typing import List
from src.domain.models.language_code import LanguageCode
from src.domain.models.media_format import MediaFormat
from src.domain.models.s3_media_file_uri import S3MediaFileUri
from src.domain.models.transcription import Transcription
from src.utils.enum_values import get_enum_values


class SedricTranscription(Transcription):
    def __init__(self, job_name: str, s3_media_file_uri: S3MediaFileUri) -> None:
        file_extension = s3_media_file_uri.get_extension()
        SedricTranscription._validate_file_extension(file_extension=file_extension)

        media_format = MediaFormat(file_extension)

        super().__init__(
            job_name=job_name,
            language_code=LanguageCode.US,
            media_format=media_format,
            media_file_uri=s3_media_file_uri,
        )

    @staticmethod
    def _validate_file_extension(file_extension: str):
        if file_extension not in SedricTranscription.allowed_media_formats():
            raise Exception(f"Not allowed file extension: {file_extension}")

    @staticmethod
    def _allowed_language_codes() -> List[str]:
        return [LanguageCode.US.value]

    @staticmethod
    def _allowed_media_formats() -> List[str]:
        return [MediaFormat.MP3.value, MediaFormat.WAV.value]
