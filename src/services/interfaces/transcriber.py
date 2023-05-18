from abc import ABC, abstractmethod
from data_transfer.transcription_request import TranscriptionRequest


class Transcriber(ABC):
    @abstractmethod
    def transcribe(self, transcription_request: TranscriptionRequest):
        ...
