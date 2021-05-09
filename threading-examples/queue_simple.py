import multiprocessing
import os
import time

POOL_COUNT = 3

def worker_main(queue):
    print os.getpid(),"working"
    while True:
        item = queue.get(True)
        print os.getpid(), "got", item
        time.sleep(1) # simulate a "long" operation


if __name__ == "__main__":
    the_queue = multiprocessing.Queue()
    the_pool = multiprocessing.Pool(POOL_COUNT, worker_main,(the_queue,))
    #                            don't forget the coma here  ^

    for i in range(9):
        the_queue.put("hello")
        # the_queue.put("world")

    # print("sleeping 5...")
    time.sleep(5)