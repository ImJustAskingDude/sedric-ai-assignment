from abc import ABC, abstractmethod
from typing import List


class SentenceFinder(ABC):
    @abstractmethod
    def find(self, transcription_text: str, sentences: List[str]):
        ...
