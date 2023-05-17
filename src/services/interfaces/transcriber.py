from abc import ABC, abstractmethod

from src.domain.models.transcription import Transcription


class Transcriber(ABC):
    @abstractmethod
    def transcribe(self, transcription: Transcription):
        ...
