from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class AwsSnsS3MessageS3Bucket:
    name: str


@dataclass(frozen=True)
class AwsSnsS3MessageS3Object:
    key: str
    size: int


@dataclass(frozen=True)
class AwsSnsS3MessageS3Field:
    bucket: AwsSnsS3MessageS3Bucket
    object: AwsSnsS3MessageS3Object


@dataclass(frozen=True)
class AwsSnsS3MessageRecord:
    s3: AwsSnsS3MessageS3Field


@dataclass(frozen=True)
class AwsSnsS3Message:
    Records: List[AwsSnsS3MessageRecord]
