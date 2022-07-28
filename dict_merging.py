d1 = {'a': 1, 'b': 1}
d2 = {'a': 2, 'c': 2}
d1 = {**d1, **d2}  # priority from right to left
print(d1)
