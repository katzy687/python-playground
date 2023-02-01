import sys


class UserValueError(ValueError):
    def __init__(self, msg):
        sys.tracebacklimit = 0
        super(UserValueError, self).__init__(msg)


def hi():
    print("hi")
    raise UserValueError("uh ohhh")


hi()
