from typing import List

from services.interfaces.recognizer import TranscriptionRecognizer


class SedricTranscriptionRecognizer(TranscriptionRecognizer):
    def __init__(self) -> None:
        pass

    def recognize(self, transcription_text: str, sentences: List[str]):
        pass
