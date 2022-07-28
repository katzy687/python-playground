import os

parent_dir = r"C:\Users\natti.k\code\python-playground\os_walk"
for root, directories, filenames in os.walk(parent_dir):
    print(f"root: {root}")
    print(f"dirs: {directories}")
    print(f"filenames: {filenames}")
