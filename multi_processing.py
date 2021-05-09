import threading

class DemoMessenger(threading.Thread):
    def run(self):
        for _ in range(10):
            print(threading.currentThread().getName() + "\n")



x = DemoMessenger(name="send")
y = DemoMessenger(name="receive")
y.start()
x.start()
pass


