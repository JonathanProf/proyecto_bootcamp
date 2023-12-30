import logging
import os
from  utilities.FileHandler import FileHandler

class ReportGeneration:
    """
    This class allows to generate the reports of each mission
    """

    def __init__(self, folder_path):
        """
        folder_path: str = this variable allows us to locate the directory where the files to be analyzed
        """
        self.folder_path = folder_path
    
    def read_files(self, ) -> None:

        files = os.listdir(self.folder_path)
        files = [file for file in files if file.endswith(".log")]

        logging.debug( files )

        for filename in files:
            if filename.endswith('.log'):
                filename = os.path.join(self.folder_path, filename)
                file = FileHandler(filename)

                if file.file_exists() is True:
                    logging.debug( f'{filename} exists? {file.read_string()}' )