from utilities.FileHandler import FileHandler
import os

directory = os.path.join('sistema_monitoreo_apollo_11', 'devices')
filename = "APLORBONE-0001.log"
full_path = os.path.join(directory, filename)

print(full_path)


file = FileHandler(full_path)

print(f"El archivo existe? {file.file_exists()} ")

texto = file.read_string()
print(texto)
