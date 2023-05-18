class SentenceKey:
    def __init__(self, sentence: str, start_index: int) -> None:
        self._sentence = sentence
        self._start_index = start_index
        self._end_index = self._start_index + len(self._sentence)

    def get_sentence(self) -> str:
        return self._sentence
    
    def get_start_index(self) -> int:
        return self._start_index
    
    def get_end_index(self) -> int:
        return self._end_index