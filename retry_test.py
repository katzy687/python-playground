import time

from retrying import retry, RetryError


def retry_if_true(result):
    return True


@retry(stop_max_attempt_number=3, wait_fixed=1000)
def my_func():
    print("doing stuff")
    raise Exception("woops")
    return "x"


try:
    my_func()
except RetryError as e:
    print(type(e).__name__)
    print(str(e))
