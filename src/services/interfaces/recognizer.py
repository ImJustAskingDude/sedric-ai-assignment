from abc import ABC, abstractmethod
from typing import List


class TranscriptionRecognizer(ABC):
    @abstractmethod
    def recognize(self, transcription_text: str, sentences: List[str]):
        ...
