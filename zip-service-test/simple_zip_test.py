import json
from zipfile import ZipFile, ZipInfo
import json

def get_zip_contents(zip_path):
    zip = ZipFile(zip_path, 'r')
    contents = zip.namelist()
    return contents


if __name__ == "__main__":
    # path = r"C:\Users\natti.k\Downloads\Postconfig_faulty.zip"
    # path = r"C:\Users\natti.k\Downloads\Postconfig_faulty2.zip"
    path = r"C:\Users\natti.k\Downloads\Postconfig.zip"
    x = get_zip_contents(path)
    print(json.dumps(x, indent=4))