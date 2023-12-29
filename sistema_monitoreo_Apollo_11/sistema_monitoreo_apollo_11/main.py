from utilities.FileHandler import FileHandler
from utilities.FilenameGenerator import FilenameGenerator
import os

directory = os.path.join('sistema_monitoreo_apollo_11', 'devices')
filename = "APLORBONE-0001.log"
full_path = os.path.join(directory, filename)

print(f'Ruta del archivo ' + full_path)

# Read file
file = FileHandler(full_path)

print(f"El archivo existe? {file.file_exists()} ")

text = file.read_string()
print(f'El contenido del archivo es:\n{text}')

# Write file
filename = FilenameGenerator(directory)
filename = filename.filename_generator()
full_path = os.path.join(directory, filename)
file = FileHandler(full_path)
text_to_write = "101223122315,OrbitOne,satellite,warning,e3c810288d28b5ff85fc35dda07329970d1a01e273c37481326fe0c861c18142"
file.write_file(text_to_write)
print(f"El archivo existe? {file.file_exists()} ")
