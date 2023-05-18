from dataclasses import dataclass

from botocore.response import StreamingBody


@dataclass(frozen=True)
class AwsS3GetObjectResponse:
    Body: StreamingBody