foo = 1
def set():
    foo = 2 # new local foo

def blub():
    # global foo
    foo = 3

for i in range(3):
    foo += i

blub()
print(foo)