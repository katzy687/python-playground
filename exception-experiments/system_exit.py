"""
SystemExit and sys.exit(1) are pretty much the same thing
sys.exit() internally raises SystemExit
"""
import sys


class MyException(SystemExit):
    def __str__(self):
        return f"{type(self).__name__}: {self.code}"


def funky():
    sys.exit("lol")
    raise MyException("what")


try:
    funky()
except SystemExit as e:
    print(f"caught. {e}")
