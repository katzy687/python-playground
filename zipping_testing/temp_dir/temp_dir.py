import tempfile
from shutil import copyfile
import os

x = tempfile.mkdtemp()


copyfile("test.txt", os.path.join(x, "hah"))

pass