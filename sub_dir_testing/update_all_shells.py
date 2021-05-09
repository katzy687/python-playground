import os
import subprocess


def install_shell(dir_name):
    my_path = os.path.abspath(__file__)
    mydir = os.path.dirname(my_path)
    shell_dir_path = os.path.join(mydir, dir_name)
    subprocess.call("cd {}".format(shell_dir_path), shell=True)
    print("cd into shell dir: '{}'".format(dir_name))
    subprocess.call(["shellfoundry", "install"])
    print("===========================")


directories_in_curdir = [d for d in os.listdir(os.curdir) if os.path.isdir(d)]
if not directories_in_curdir:
    raise Exception("No subdirectories in this folder")

for shell_dir in directories_in_curdir:
    install_shell(shell_dir)
