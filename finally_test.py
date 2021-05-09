from time import sleep
try:
    raise Exception("fuck!")
except Exception as e:
    print("uh oh an exception!")
    sleep(2)
    raise
finally:
    print("finally!")
    sleep(2)

