import cProfile
from time import sleep
# cProfile.run("2 + 2")


def func_a():
    sleep(1)
    print("hi from A")


def func_b():
    print("hi from B")
    sleep(2)
    func_a()


def func_c():
    print("hi from C")
    sleep(3)
    func_b()


cProfile.run('func_c()')