from enum import Enum


class MyEnum(Enum):
    VAL_1 = "hi"
    VAL_2 = "bye"


print(isinstance("hi", MyEnum))
values = [x for x in MyEnum]
print("hi" in values)
