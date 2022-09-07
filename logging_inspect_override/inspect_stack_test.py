import inspect


def my_wrapper():
    stack = inspect.stack()
    target_stack = stack[0]
    function = target_stack.function
    line_number = target_stack.lineno
    file_name = target_stack.filename
    pass


def main_code_helper():
    my_wrapper()


def main():
    main_code_helper()


if __name__ == "__main__":
    main()