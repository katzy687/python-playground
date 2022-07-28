import os

current_path = os.getcwd()
test_dir_path = os.path.join(current_path, "test")
if not os.path.isdir(test_dir_path):
    print("making dir")
    os.mkdir(test_dir_path)