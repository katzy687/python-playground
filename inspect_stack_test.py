import inspect
import sys

stack = inspect.stack()


def a():
    python_major_version = sys.version_info.major

    stack = inspect.stack()
    target_stack = stack[0]
    function = target_stack.function
    line_number = target_stack.lineno
    file_name = target_stack.filename
    pass


def b():
    a()


def c():
    b()

c()