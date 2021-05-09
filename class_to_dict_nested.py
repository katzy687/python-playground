import json


class RandomObj(object):
    def __init__(self, attr1, attr2):
        self.attr1 = attr1
        self. attr2 = attr2


class MyClass(object):
    def __init__(self, attr1, attr2, attr3):
        self.attr1 = attr1
        self.attr2 = attr2
        self.attr3 = attr3
        self.attr4 = []


random_obj = RandomObj(1, 2)
random_obj2 = RandomObj(3, random_obj)
random_obj3 = RandomObj(3, random_obj2)
random_obj4 = RandomObj(3, random_obj3)

my_obj = MyClass("a", "b", random_obj4)
print(my_obj.__dict__)
x = getattr(my_obj, "__dict__", 4)


def get_json_recursive(obj):
    return json.dumps(obj, default=lambda o: getattr(o, '__dict__', str(o)), indent=4)


my_json = get_json_recursive(my_obj)
print(my_json)

