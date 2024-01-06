import logging
import os
from  utilities.FileHandler import FileHandler
import pandas as pd
from tabulate import tabulate

class ReportGeneration:
    """
    This class allows to generate the reports of each mission
    """

    def __init__(self, folder_path):
        """
        folder_path: str = this variable allows us to locate the directory where the files to be analyzed
        """
        self.folder_path = folder_path
        self.debug = False
    
    def read_files(self, ) -> None:

        if self.debug == True:
            self.folder_path = os.path.join('sistema_monitoreo_Apollo_11', 'sistema_monitoreo_Apollo_11', 'devices')

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

        if self.debug == True:
            self.dataframe.to_csv('output.csv', index=False)
        logging.info(self.dataframe)
    
    def disconnections_report(self) -> str:

        df2 = self.dataframe[self.dataframe["device_status"] == 'unknown']

        msg = f'Cantidad de desconexiones encontradas {len(df2)}\n'
        msg += f'{"="*50}\n'
        msg += "Desconexiones reportadas por misión\n"
        msg += f'{"="*50}\n'

        for device, value in df2.groupby('device_type')['device_status'].count().to_dict().items():
            msg += f'Hay {value} desconexiones para el dispositivo {device}\n'
        
        msg += f'{"="*50}\n'
        
        logging.info(msg)
        return msg

    def event_analysis(self) -> str:
        
        dict_report = self.dataframe.groupby(by=['mission', 'device_type', 'device_status'])['device_status'].count().to_dict()

        msg = f'{"="*50}\n'
        msg += "Analisis de eventos por estado para cada misión y dispositivo\n"
        
        
        msg += "| {0} | {1} | {2} | {3} |\n".format('Mission'.center(20), 'Device Type'.center(20), 'Device Status'.center(20), 'Event Occurrence Number'.center(20))
        msg += f'{"-"*95}\n'
        for k, event_occurrence_number in dict_report.items():
            mission, device_type, device_status = k
            msg += "| {0} | {1} | {2} | {3} |\n".format(mission.center(20), device_type.center(20), device_status.center(20), str(event_occurrence_number).center(23))

        msg += f'{"-"*95}\n'
        
        logging.info(msg)
        return msg

        
