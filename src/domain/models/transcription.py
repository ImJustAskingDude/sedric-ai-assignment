from typing import List

from domain.models.language_code import LanguageCode
from domain.models.media_file_uri import MediaFileUri
from domain.models.media_format import MediaFormat
from utils.enum_values import get_enum_values


class Transcription:
    def __init__(
        self,
        job_name: str,
        language_code: LanguageCode,
        media_format: MediaFormat,
        media_file_uri: MediaFileUri,
    ) -> None:
        self._job_name = job_name
        self._language_code = language_code
        self._media_format = media_format
        self._media_file_uri = media_file_uri

    def get_job_name(self) -> str:
        return self._job_name
    
    def get_language_code(self) -> LanguageCode:
        return self._language_code
    
    def get_media_format(self) -> MediaFormat:
        return self._media_format
    
    def get_media_file_uri(self) -> MediaFileUri:
        return self._media_file_uri

    @staticmethod
    def allowed_language_codes() -> List[str]:
        return get_enum_values(LanguageCode)

    @staticmethod
    def allowed_media_formats() -> List[str]:
        return get_enum_values(MediaFormat)
