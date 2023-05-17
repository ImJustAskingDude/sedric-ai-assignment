from dataclasses import dataclass


@dataclass(frozen=True)
class RecognitionResultSentence:
    plain_text: str
    was_present: bool
    start_word_index: int
    end_word_index: int
