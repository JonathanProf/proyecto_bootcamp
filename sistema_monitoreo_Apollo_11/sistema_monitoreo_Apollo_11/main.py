from utilities.FileHandler import FileHandler
from utilities.FilenameGenerator import FilenameGenerator
from utilities.FileContentGeneration import FileContentGenerator
from utilities.ReportGeneration import ReportGeneration
import os
from datetime import datetime
import random
import logging
logging.basicConfig(format='%(asctime)s -> %(levelname)s in FILE: %(filename)s [LINE %(lineno)d] - %(message)s', level=logging.INFO)

directory = os.path.join('sistema_monitoreo_Apollo_11', 'devices')

# Inicio de simulación para generación de archivos, primero se realizará una simulación para 10 archivos y luego se escalará en las siguientes pruebas
print("===================================")
print("= Ingrese 1 para generar archivos =")
print("= Ingrese 2 para generar reporte  =")
print("===================================")
opcion_menu = int(input("Ingrese -> "))
if opcion_menu == 1:
    print("Generación de archivos")
    # Constants
    mission = {
        'ORBONE': 'OrbitOne',
        'CLNM': 'ColonyMoon',
        'TMRS': 'VacMars', 
        'GALXONE': 'GalaxyTwo', 
        'UNKN': 'Unknown'
    }
    date = datetime.now().strftime("%d%m%y%H%M%S")
    device_type = ['navigation system', 'satellite', 'main computer', 'thermal camera']
    device_status = ['excellent', 'good', 'warning', 'faulty', 'killed', 'unknown']
    for _ in range(10):

        # Content generator
        mission_selected = random.choice(list(mission.keys()))
        filename = FilenameGenerator(directory)
        filename = filename.filename_generator(mission_selected)

        content = FileContentGenerator(filename=filename, mission=mission[mission_selected], date=date, device_type= random.choice(device_type), device_status= random.choice(device_status))
        text_to_write = content.get_content()
        logging.debug(text_to_write)
        # File generator
        
        full_path = os.path.join(directory, filename)
        file = FileHandler(full_path)

        
        file.write_file(text_to_write)

elif opcion_menu == 2:
    report = ReportGeneration(directory)
    report.read_files()
else:
    print("Opcion incorrecta, intente de nuevo")


"""
filename = "APLORBONE-0001.log"
full_path = os.path.join(directory, filename)
logging.debug(f'Ruta del archivo ' + full_path)

# Read file
file = FileHandler(full_path)

logging.debug(f"El archivo existe? {file.file_exists()} ")

text = file.read_string()
logging.debug(f'El contenido del archivo es:\n{text}')
"""