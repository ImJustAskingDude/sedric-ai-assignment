from dataclasses import dataclass
from typing import List, Optional

from data_transfer.recognize_result_sentence import RecognitionResultSentence


@dataclass(frozen=True)
class RecognitionResult:
    id: str
    request_id: str
    audio_url: str
    transcription_url: Optional[str]
    sentences: List[RecognitionResultSentence]
