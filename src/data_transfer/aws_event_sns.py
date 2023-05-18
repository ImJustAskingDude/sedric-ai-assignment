from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class AwsEventSnsRecordSnsField:
    Message: str


@dataclass(frozen=True)
class AwsEventSnsRecord:
    Sns: AwsEventSnsRecordSnsField


@dataclass(frozen=True)
class AwsEventSns:
    Records: List[AwsEventSnsRecord]
