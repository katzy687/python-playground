"""
https://stackoverflow.com/a/50146869
"""
import json

import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('foo.json')
stream_handler = logging.StreamHandler()

stream_formatter = logging.Formatter(
    '%(asctime)-15s %(levelname)-8s %(message)s')
execution_info = {"host_name": "QS-IL-LT-NATTIK",
                  "IP": "1.1.1.1",
                  "Platform": "Windows",
                  "Python Version": "3.7.1"}
fmt_dict = {'time': '%(asctime)s',
            'name': '%(name)s',
            'level': '%(levelname)s',
            'message': '%(message)s',
            'function': '%(module)s.%(funcName)s - line %(lineno)d',
            'path_name': '%(pathname)s',
            'process': '%(process)d',
            'execution_info': execution_info}

file_formatter = logging.Formatter(json.dumps(fmt_dict))
file_handler.setFormatter(file_formatter)
stream_handler.setFormatter(stream_formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

def log_it():
    logger.info("'hello there'")

log_it()
