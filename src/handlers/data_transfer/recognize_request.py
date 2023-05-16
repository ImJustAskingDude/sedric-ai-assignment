from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class RecognizeRequest:
    audio_url: str
    sentences: List[str]