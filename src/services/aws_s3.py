from typing import Any, Dict
import boto3
import jsons

from data_transfer.aws_s3_get_object_response import AwsS3GetObjectResponse


class AwsS3:
    def __init__(self) -> None:
        self._client = boto3.client("s3")

    def get_object(self, bucket_name: str, path_name: str) -> AwsS3GetObjectResponse:
        return jsons.load(
            self._get_object(bucket_name=bucket_name, path_name=path_name),
            AwsS3GetObjectResponse,
        )

    def _get_object(self, bucket_name: str, path_name: str) -> Dict[str, Any]:
        return self._client.get_object(Bucket=bucket_name, Key=path_name)
