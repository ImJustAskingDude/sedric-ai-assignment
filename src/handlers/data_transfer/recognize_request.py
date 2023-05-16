from dataclasses import dataclass
from typing import List

@dataclass
class RecognizeRequest:
    audio_url: str
    sentences: List[str]