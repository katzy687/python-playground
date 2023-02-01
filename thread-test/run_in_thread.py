import time
from time import sleep
import threading


def run_command():
    while True:
        print(f"running in thread {time.time()}")
        sleep(1)


def run_in_thread():
    my_thread = threading.Thread(target=run_command, daemon=True)
    my_thread.start()
    my_thread.join(timeout=5)
    print("done")


if __name__ == "__main__":
    run_in_thread()
