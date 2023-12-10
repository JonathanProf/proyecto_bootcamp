import os

class FileHandler:

    def __init__(self, file_path):
        self.file_path = file_path

    def file_exists(self) -> bool:
        """Determine if a file exists"""
        return os.path.exists(self.file_path)

    def read_string(self) -> str:
        """Read the string format of a file"""
        with open(self.file_path, "r") as file:
            return file.read()