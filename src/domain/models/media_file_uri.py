class MediaFileUri:
    def __init__(self, file_name: str) -> None:
        self._file_name = file_name

    def get_file_name(self) -> str:
        return self._file_name