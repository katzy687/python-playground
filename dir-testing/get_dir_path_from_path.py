import os


def get_dir_from_abs_path(abs_path):
    path = os.path.normpath(abs_path)
    path_components = path.split(os.sep)
    current_dir = os.path.join(*path_components[:-1])
    return current_dir

if __name__ == "__main__":
    file_name = "test_file.txt"
    my_abs_path = os.path.abspath(file_name)
    print(get_dir_from_abs_path(my_abs_path))