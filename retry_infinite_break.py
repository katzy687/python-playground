"""
https://pypi.org/project/retrying/
"""
from time import sleep

from retrying import retry


@retry(wait_fixed=1000, stop_max_delay=3000)
def check_dhcp():
    while True:
        print("running")
        raise Exception("oh no")


@retry(wait_fixed=1000, stop_max_delay=5000)
def do_something_crazy():
    print("doing something crazy")
    return True


if __name__ == "__main__":
    check_dhcp()
