from datetime import datetime

class FileContentGenerator:

    def __init__(self, filename: str, mission: str, date: datetime, device_type: str, device_status: str):
        
        self.filename = filename
        self.mission = mission
        self.date = date
        self.device_type = device_type
        self.device_status = device_status

    def get_content(self) -> str:
        
        if self.filename.find('UNKN') == -1:
            self.hash = str(hash((self.date, self.mission, self.device_type, self.device_status)))
            return self.date + ',' + self.mission + ',' + self.device_type + ',' + self.device_status + ',' + self.hash
        else:
            return self.date + ',' + self.mission + ',' + 'unknown' + ',' + 'unknown' + ',' + 'unknown'

