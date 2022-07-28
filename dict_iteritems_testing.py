import sys
my_dict = {"key1": "val1"}

# PY2
for key, value in my_dict.iteritems():
    print(key, value)

# PY3
for key, value in my_dict.items():
    print(key, value)