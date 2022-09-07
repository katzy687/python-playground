from multiprocessing.dummy import Pool as ThreadPool
import threading
from time import sleep
import os


def my_function(num):
    print("'{}' - working: {}".format(num, threading.current_thread().name))
    sleep(num * num)
    print("=== '{}' - done: {} ===".format(num, threading.current_thread().name))
    if num == 2:
        raise Exception("ummm")
    else:
        return num
    # return num


if __name__ == "__main__":
    my_array = [2, 3, 4]
    pool = ThreadPool(2)
    results = [(x, pool.apply_async(my_function, (x,))) for x in my_array]
    pool.close()
    pool.join()
    failed = []
    for x, result in results:
        try:
            z = result.get()
        except:
            failed.append(x)
    if failed:
        raise Exception("Failed: {}".format(failed))