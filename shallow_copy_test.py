tuple_list = [("key1", "value1"), ("key2", "value2"), ("key3", "value3")]
copied = tuple_list[:]

tuple_list[0] = "lol"
print(tuple_list[0])
print(copied[0])