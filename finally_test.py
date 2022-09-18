import time


def work():
    try:
        raise Exception("what???")
    except Exception as e:
        print("Caught Exception")
        time.sleep(2)
        raise
    else:
        print("success??")
    finally:
        print("running finally")


work()