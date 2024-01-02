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
        
        self.dataframe = pd.DataFrame(data_table, columns=['date', 'mission', 'device_type', 'device_status', 'hash'])
        logging.info(self.dataframe)
    
    def disconnections_report(self) -> None:

        df2 = self.dataframe[self.dataframe["device_status"] == 'unknown']

        logging.info(f'Cantidad de desconexiones encontradas {len(df2)}')

        logging.info("Desconexiones reportadas por misión")

        for device, value in df2.groupby('device_type')['device_status'].count().to_dict().items():
            logging.info(f'Hay {value} desconexiones para el dispositivo {device}')
