from os import path
from src.domain.models.media_file_uri import MediaFileUri


class S3MediaFileUri(MediaFileUri):
    def __init__(self, bucket_name: str, file_name: str) -> None:
        S3MediaFileUri._validate_file_name(file_name=file_name)

        super().__init__(f"s3://{bucket_name}/{file_name}")

        self._only_file_name = file_name

    def get_extension(self) -> str:
        return path.splitext(self._only_file_name)[1][1:]
    
    @staticmethod
    def _validate_file_name(file_name: str):
        if file_name.replace(' ', '') == '':
            raise Exception('File name must not be empty')

        if file_name.strip() != file_name:
            raise Exception('File name must not contain spaces')
        
        if file_name.find('.') == -1:
            raise Exception('File must have an extension')