"""
https://stackoverflow.com/questions/46318714/how-do-i-generate-a-python-timestamp-to-a-particular-format
"""


import datetime
date = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
print(date)