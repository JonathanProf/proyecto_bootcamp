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


    def event_analysis(self) -> str:
        """
        b) Análisis de eventos
        Se deberá realizar un análisis de la cantidad de eventos por estado para
        cada misión y dispositivo.
        """
        
        dict_report = self.dataframe.groupby(by=['mission', 'device_type', 'device_status'])['device_status'].count().to_dict()

        msg = f'\n{"="*100}\n'
        msg += "Analisis de eventos por estado para cada misión y dispositivo".center(100)
        msg += f'\n{"="*100}\n\n'
        
        table = []
        for k, event_occurrence_number in dict_report.items():
            row = list(k)
            row.append(event_occurrence_number)
            table.append(row)

        msg += tabulate(table, headers=['Mission', 'Device Type', 'Device Status', 'Number Unknown Devices'], tablefmt="grid")
        
        logging.info(msg)
        return msg
    
    
    def disconnections_report(self) -> str:
        """
        c) Gestión de desconexiones
        Es necesario identificar los dispositivos que presentan un mayor número
        de desconexiones, específicamente en el estado "unknown", para cada
        misión.
        """

        df2 = self.dataframe[self.dataframe["device_status"] == 'unknown']

        msg = f'\n{"="*100}\n'
        msg = f'Cantidad de desconexiones encontradas {len(df2)}'.center(100)
        msg += f'\n{"="*100}\n'
        msg += "Desconexiones reportadas por misión".center(100)
        msg += f'\n{"="*100}\n'

        for device, value in df2.groupby('device_type')['device_status'].count().to_dict().items():
            msg += f'Hay {value} desconexiones para el dispositivo {device}\n'
        
        msg += f'\n{"="*100}\n'
        
        logging.info(msg)
        return msg       

    def mission_consolidation(self) -> str:
        """
        d) Consolidación de misiones
        Debe realizarse la consolidación de todas las misiones para determinar
        cuántos dispositivos son inoperables.
        """
        df_consolidation = self.dataframe[self.dataframe["device_status"] == 'killed']
        dict_report = df_consolidation.groupby(['mission', 'device_type'])['device_status'].count().to_dict()

        table = []
        msg = f'\n\n{"="*100}\n'
        msg += "Consolidación de misiones para dispositivos inoperables".center(100)
        msg += f'\n{"="*100}\n'
        for k, event_occurrence_number in dict_report.items():
            row = list(k)
            row.append(event_occurrence_number)
            table.append(row)

        msg += tabulate(table, headers=['Mission', 'Device Type', 'Number Killed Devices'], tablefmt="grid")
        msg += f'\n{"="*100}\n'

        logging.info(msg)
        return msg