from collections import OrderedDict

my_dict = {"1": "lol", "3": "okay", "2": "HA!", "NA": []}
x = OrderedDict(sorted(my_dict.items()))
print(x)

