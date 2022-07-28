import zipfile
import os
x = os.path.join("xyz", "wtf")
os.makedirs(x)
os.mkdir("my_dir/test")
with zipfile.ZipFile("my_dir/test.zip", 'w') as zip_ref:
    zip_ref.write("test_it.txt")
