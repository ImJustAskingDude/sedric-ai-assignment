from typing import Dict, List
from domain.models.sentence_key import SentenceKey

from services.interfaces.sentence_finder import SentenceFinder

SentenceType = str


class SedricSentenceFinder(SentenceFinder):
    def __init__(self) -> None:
        pass

    def find(
        self, transcription_text: str, sentences: List[str]
    ) -> Dict[SentenceType, List[SentenceKey]]:
        sentences = set(sentences)
        sentence_keys: Dict[SentenceType, List[SentenceKey]] = {}

        for sentence in sentences:
            start_index = transcription_text.find(sentence)
            sentence_keys[sentence] = []

            while start_index != -1:
                sentence_keys[sentence].append(
                    SentenceKey(sentence=sentence, start_index=start_index)
                )

                next_start_index = start_index + len(sentence)
                start_index = transcription_text.find(sentence, next_start_index)

        return sentence_keys
