import logging
import inspect
import os


def myMakeRecord(name, level, fn, lno, msg, args, exc_info, func, extra, sinfo):
    rv = logging.LogRecord(name, level, fn, lno, msg, args, exc_info, func, sinfo)
    if extra is not None:
        rv.__dict__.update(extra)
    return rv


def mylog(logger, msg, level, *args):
    logging.Logger.makeRecord = myMakeRecord
    frame = inspect.currentframe()
    caller = frame.f_back
    override = {
        "lineno":caller.f_lineno,
        "filename":os.path.basename(caller.f_code.co_filename),
    }
    logger.log(level, msg, extra=override, *args)


logger = logging.getLogger("test")
my_handler = logging.StreamHandler()
logger.addHandler(my_handler)
my_formatter = logging.Formatter()
mylog(logger, "lol.txt", logging.INFO)