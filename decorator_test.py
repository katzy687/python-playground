import inspect
import sys
from functools import wraps
import time

def my_decorator(f):
    @wraps(f)
    def wrapper(*args,**kwargs):
        print("calling decorator")
        return f(*args, **kwargs)
    return wrapper



# @wraps()
# def wrapper(*args,**kwargs):
#     print("calling decorator")

def qs_time_this(func):
    """Decorator that reports the execution time."""  # noqa: D202
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        print("%s started" % func.__name__)
        time.sleep(3)
        result = func(*args, **kwargs)
        end = time.time()
        print("%s ended taking %s" % (func.__name__, str(end - start)))
        return result

    return wrapper

class TestClass(object):
    def qs_time_this(self, func):
        """Decorator that reports the execution time."""  # noqa: D202

        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            print("%s started" % func.__name__)
            time.sleep(3)
            result = func(*args, **kwargs)
            end = time.time()
            print("%s ended taking %s" % (func.__name__, str(end - start)))
            return result

        return wrapper


# reporter = TestClass()


def test():
    """Hello There"""
    print("Calling test func.")

# test()
# wrapper()

class MyClass(object):

    def __init__(self):
        self.reporter = TestClass()

    def test(self):
        print("hello from class test")

# MyClass().test()

# qs_time_this(test)()
# reporter = TestClass()
# reporter.qs_time_this(test)()


def test_sys_get_frame():
    stack = inspect.stack()
    print inspect.stack()[1][3]

def x():
    test_sys_get_frame()

def yoo():
    this_function_name = inspect.currentframe().f_code.co_name
    print("name is: " + this_function_name)
    x()

# yoo()

# print sys.version_info.major
# test()
# print(test.__name__)
# print(test.__doc__)

class Test(object):
    def _decorator(foo):
        def magic( self ) :
            print "start magic"
            foo( self )
            print "end magic"
        return magic

    @_decorator
    def bar( self ) :
        print "normal call"

class TestWraps(object):
    def hello(self, message):
        print("hello " + message)
        # print("func_name: " + self.hello.__name__)

def lol():
    x = TestWraps()
    x.hello("yo")


def rename_func_to_parent(f):
    current_frame = inspect.currentframe(1)
    curr_func = sys._getframe(0).f_code
    stack = inspect.stack()
    parent_func_name = stack[2][3]
    f.__name__ = parent_func_name
    # return f


def rename_test(func):
    def wrapper():
        stack = inspect.stack()
        parent_func = stack
        print("renaming func in wrapper...")
        func.__name__ = "lolll"
        func()
    return wrapper


def print_stack(f):
    print("inside {}".format(f.__name__))
    stack = inspect.stack()
    for item in stack:
        print(item[3])
    print("==========")


# @rename_func_to_parent
def f():
    # stack = inspect.stack()
    # parent_func_name = stack[1][3]
    # f.__name__ = parent_func_name
    rename_func_to_parent(f)
    print("logging for target function: {}".format(f.__name__))


def g():
    # print_stack(g)
    f()

# f = rename_func_to_parent(f)

# x = rename_func_to_parent()(f)
# print x.__name__
# print f.__name__
g()

# f = rename("loll")(f)
# print(f.__name__)
# x = TestWraps()
# print(x.hello.__name__)
