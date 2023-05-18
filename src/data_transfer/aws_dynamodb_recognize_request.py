from dataclasses import dataclass
from datetime import datetime
from typing import List


@dataclass(frozen=True)
class AwsDynamoDbRecognizeRequest:
    requestId: str
    audioFileUrl: str
    requestTime: datetime
    sentences: List[str]