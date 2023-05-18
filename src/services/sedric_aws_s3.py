import jsons

from data_transfer.transcription_result_file_content import (
    TranscriptionResultFileContent,
)
from services.aws_s3 import AwsS3


class SedricAwsS3(AwsS3):
    def __init__(self) -> None:
        super().__init__()

    def get_transcription(self, request_id: str) -> TranscriptionResultFileContent:
        response = self.get_object(
            bucket_name="sedric-transcription-results", path_name=f"{request_id}.json"
        )
        file_content_body = response.Body.read().decode()
        return jsons.loads(file_content_body, TranscriptionResultFileContent)
