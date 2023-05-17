from dataclasses import dataclass


@dataclass(frozen=True)
class RecognizeResponseBody:
    request_id: str
    message: str