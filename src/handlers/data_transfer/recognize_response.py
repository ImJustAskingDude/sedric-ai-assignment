from dataclasses import dataclass
from src.handlers.data_transfer.recognize_response_body import RecognizeResponseBody

@dataclass(frozen=True)
class RecognizeResponse:
    body: RecognizeResponseBody