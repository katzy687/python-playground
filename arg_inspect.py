import inspect

def my_func(param1, param2):
    pass


class my_class(object):
    def lol(self, param1, param2):
        pass

    @staticmethod
    def haha():
        pass


def is_bound(m):
    return hasattr(m, '__self__')

args = inspect.getargspec(my_func).args

for curr_arg in args:
    print curr_arg

x = my_class()

print(is_bound(x.lol))
print(is_bound(x.haha))
print(is_bound(my_func))

