import os
import shutil

source_dir = r'C:\Users\natti.k\code\python-playground\dir-testing\shutil_tests\test_dir'
destination_dir = r"C:\Users\natti.k\code\python-playground\dir-testing\shutil_tests\destination\random"
if os.path.exists(destination_dir):
    shutil.rmtree(destination_dir)
shutil.copytree(source_dir, destination_dir)
