from retrying import retry, RetryError


def validation_func(result):
    return True


@retry(wait_fixed=1000, stop_max_delay=5000, retry_on_result=validation_func)
def do_something_crazy():
    print("doing something crazy")
    return True

@retry(wait_fixed=1000, stop_max_delay=5000)
def exception_test():
    print("doing something crazy")
    raise Exception("woops")
    # return True

exception_test()

