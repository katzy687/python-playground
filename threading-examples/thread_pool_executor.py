# SuperFastPython.com
# example of the submit and wait for all pattern for the ThreadPoolExecutor
from time import sleep
from random import randint
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import wait


# custom task that will sleep for a variable amount of time
def task(name):
    # sleep for less than a second
    randy_int = randint(1, 3)
    sleep(randy_int)
    # if randy_int == 2:
    #     raise Exception(f"{name} got randy int 2!!!!")
    # display the result
    return name



with ThreadPoolExecutor(10) as executor:
    # submit tasks and collect futures
    futures = [executor.submit(task, i) for i in range(10)]
    # wait for all tasks to complete
    res = wait(futures)
    for f in res.done:
        res = f.result()
        print(res)
        pass
    print('All tasks are done!')
