from dataclasses import dataclass
from enum import Enum
from typing import Optional


class HttpMethod(Enum):
    POST = "POST"
    GET = "GET"


@dataclass(frozen=True)
class AwsEvent:
    resource: str
    path: str
    httpMethod: HttpMethod
    body: Optional[str]
    isBase64Encoded: bool
