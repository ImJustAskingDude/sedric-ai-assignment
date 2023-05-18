from dataclasses import dataclass
from typing import List, Optional

from data_transfer.recognize_result_sentence import RecognitionResultSentence


@dataclass(frozen=True)
class RecognitionResult:
    resultId: str
    requestId: str
    audioUrl: str
    transcriptionUrl: Optional[str]
    sentences: List[RecognitionResultSentence]
