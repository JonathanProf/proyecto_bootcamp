import logging
import os
from  utilities.FileHandler import FileHandler
import pandas as pd

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
        files.sort()

        logging.debug( files )

        data_table = []

        for filename in files:
            if filename.endswith('.log'):
                filename = os.path.join(self.folder_path, filename)
                file = FileHandler(filename)

                if file.file_exists() is True:
                    logging.debug( f'{filename} exists? {file.read_string()}' )

                    data = file.read_string().split(',')
                    data_table.append(data)
        
        df = pd.DataFrame(data_table, columns=['date', 'mission', 'device_type', 'device_status', 'hash'])
        logging.debug(df)
