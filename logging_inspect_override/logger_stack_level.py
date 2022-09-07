import inspect
import logging
import sys
import inspect

DEFAULT_FORMAT = (
    "%(asctime)s [%(levelname)s]: %(name)s %(module)s - %(funcName)-20s %(message)s"
)

def get_logger():
    logger = logging.getLogger("test")
    logger.setLevel(logging.INFO)
    my_handler = logging.StreamHandler(stream=sys.stdout)
    formatter = logging.Formatter(DEFAULT_FORMAT)
    my_handler.setFormatter(formatter)
    logger.addHandler(my_handler)
    return logger


def my_wrapper(logger: logging.Logger):
    logger.info("Hello from inside function")
    sig = inspect.getfullargspec(logger._log)
    if "stacklevel" in sig.args:
        logger.info("Hello from function, but adjusting stack", stacklevel=2)


logger = get_logger()
my_wrapper(logger)
logger.info("hello from top level")
