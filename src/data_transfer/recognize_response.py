from dataclasses import dataclass

from data_transfer.recognize_response_body import RecognizeResponseBody


@dataclass(frozen=True)
class RecognizeResponse:
    body: RecognizeResponseBody
