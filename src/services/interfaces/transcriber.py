from abc import ABC, abstractmethod

from domain.models.transcription import Transcription


class Transcriber(ABC):
    @abstractmethod
    def transcribe(self, transcription: Transcription, output_bucket_name: str, output_key: str):
        ...
