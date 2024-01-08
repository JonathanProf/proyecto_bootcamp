import os
import logging

class FileHandler:

    def __init__(self, directory_path: str, filename: str):

        if not os.path.isdir(directory_path):
            os.makedirs(directory_path, exist_ok=True)
            logging.debug(f"Folder creation {directory_path}")
            

        self.file_path = os.path.join(directory_path, filename)

    def file_exists(self) -> bool:
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
        try:
            with open(self.file_path, "w") as file:
                return file.write(text)
        except:
            logging.error('Cannot open file')
            return None