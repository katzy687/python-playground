from builtins import function

class Sandbox(object):
    pass


class CustomSandbox(Sandbox):
    pass


def my_func():
    pass

print(type(my_func))

x = Sandbox()
y = CustomSandbox()


if type(y) is CustomSandbox:
    print("Yes")
else:
    print("no")