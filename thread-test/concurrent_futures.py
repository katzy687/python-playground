import concurrent.futures
import os
import time


# Define a function that will be run in a separate thread
def slow_function(n):
    print("started thread")
    time.sleep(n)
    return n


def infinite_function():
    print("started infinite")
    infinite_pid = os.getpid()
    print(f"inf pid: {infinite_pid}")
    while True:
        print("running infinite")
        time.sleep(1)


# Create a thread pool with a single thread
with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
    main_pid = os.getpid()
    print(f"main pid: {main_pid}")
    # Submit a task to the thread pool
    future = executor.submit(slow_function, 5)
    future2 = executor.submit(infinite_function)

    try:
        result1 = future.result(timeout=6)
        result2 = future2.result(timeout=6)
    except concurrent.futures.TimeoutError:
        print("TimeoutError: The tasks did not complete within the specified timeout")
    else:
        print(f"Result: {result1}")
        print(f"Result: {result2}")
    print("kill main pid")
    os.kill(main_pid, 9)
