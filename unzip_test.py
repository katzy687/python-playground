import os
import zipfile
import shutil
import tempfile

print("Creating one temporary file...")

temp = tempfile.TemporaryFile() #2

try:
    print("Created file is:", temp) #3
    print("Name of the file is:", temp.name) #4
finally:
    print("Closing the temp file")
    temp.close() #5

with zipfile.ZipFile(file_path, 'r') as zip_ref:
    zip_ref.extractall(full_path_base_dir)
