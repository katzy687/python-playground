import json


class MyClass(object):
    def __init__(self, attr1, attr2, attr3):
        self.attr1 = attr1
        self.attr2 = attr2
        self.attr3 = attr3
        self.attr4 = []


my_obj = MyClass("a", "b", "c")
print(json.dumps(my_obj.__dict__, indent=4))