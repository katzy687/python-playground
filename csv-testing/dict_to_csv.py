import csv
import io
from tempfile import TemporaryFile


somedict = dict(raymond='red', rachel='blue', matthew='green')


# with open('mycsvfile.csv', 'w', newline="") as f:
#     w = csv.writer(f)
#     w.writerows(somedict.items())

with open(TemporaryFile().name, 'w', newline="") as f:
    w = csv.writer(f)
    w.writerows(somedict.items())
