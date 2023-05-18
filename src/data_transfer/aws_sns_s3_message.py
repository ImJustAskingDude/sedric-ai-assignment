from dataclasses import dataclass


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
class AwsSnsS3Message:
    s3: AwsSnsS3MessageS3Field
