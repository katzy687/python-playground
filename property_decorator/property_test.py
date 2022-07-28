class MyClass:
    def __init__(self, my_param):
        self._my_param = my_param

    @property
    def my_param(self):
        return self._my_param

    @my_param.setter
    def my_param(self, value):
        self._my_param = value


x = MyClass("lol")
print(x.my_param)
x.my_param = "hey"
print(x.my_param)
