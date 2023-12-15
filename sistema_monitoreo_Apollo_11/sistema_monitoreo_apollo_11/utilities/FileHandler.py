import os
import logging

logging.basicConfig(format='%(asctime)s -> %(levelname)s in FILE: %(filename)s [LINE %(lineno)d] - %(message)s', level=logging.DEBUG)

class FileHandler:

    def __init__(self, file_path):
        self.file_path = file_path

    def file_exists(self) -> any:
        """Determine if a file exists"""
        return os.path.exists(self.file_path)

    def read_string(self) -> str:
        """Read the string format of a file"""
        try:
            with open(self.file_path, "r") as file:
                return file.read()
        except:
            logging.error('Cannot read file')
            return None
            
    
    def write_file(self, text: str) -> bool:
        """Write text to the file"""
        with open(self.file_path, "w") as file:
            return file.write(text)