import inspect
import sys

stack = inspect.stack()


def wrapper():

    stack = inspect.stack()
    target_stack = stack[0]
    function = target_stack.function
    line_number = target_stack.lineno
    file_name = target_stack.filename
    pass


def main_code_helper():
    wrapper()


def main_code():
    main_code_helper()

main_code()