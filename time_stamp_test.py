"""
https://stackoverflow.com/questions/46318714/how-do-i-generate-a-python-timestamp-to-a-particular-format
"""
import datetime


def get_timestamp():
    return datetime.datetime.now().strftime("%d-%m-%YT%H:%M:%S")


print(get_timestamp())