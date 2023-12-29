import logging
import random

logging.basicConfig(format='%(asctime)s -> %(levelname)s in FILE: %(filename)s [LINE %(lineno)d] - %(message)s', level=logging.DEBUG)

class FilenameGenerator:
    """
    This class allows to generate the filename in a random way for the simulation execution according to the following format
    APL[ORBONE|CLNM|TMRS|GALXONE|UNKN]-0000[1-1000].log
    """

    def __init__(self, folder_path):
        self.mission = {
            'ORBONE': 'OrbitOne',
            'CLNM': 'ColonyMoon',
            'TMRS': 'VacMars', 
            'GALXONE': 'GalaxyTwo', 
            'UNKN': 'Unknown'
        }
        self.folder_path = folder_path

    def filename_generator(self) -> str:
        mission_selected = random.choice(list(self.mission.keys()))
        mission_number = random.randint(1, 1000)
        filename = 'APL{0}-0000{1:04d}.log'.format(mission_selected, mission_number)
        
        return filename

