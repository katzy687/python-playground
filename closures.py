x = 1


def fun():
    global x
    # x = 0
    x += 1

fun()
print(x)