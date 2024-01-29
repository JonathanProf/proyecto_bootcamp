import random


class FilenameGenerator:
    """
    This class allows to generate the filename in a random way for the simulation
    execution according to the following format
    APL[ORBONE|CLNM|TMRS|GALXONE|UNKN]-0000[1-1000].log
    """

    def __init__(self, folder_path):

        self.folder_path = folder_path

    def filename_generator(self, mission: str) -> str:

        mission_number = random.randint(1, 1000)
        filename = 'APL{0}-0000{1:04d}.log'.format(mission, mission_number)

        return filename

    def filename_generator_report(self, date: str) -> str:

        filename = 'APLSTATS-REPORTE-{0}.log'.format(date)

        return filename
