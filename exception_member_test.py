import inspect


class MyException(Exception):
    pass


class MySecondException(Exception):
    def __init__(self, msg):
        self.msg = msg,
    def __str__(self):
        return "self error type is " + str(type(self).__name__)


my_excs = [MyException, MySecondException]

# try:
#     raise MyException
# except Exception as e:
#     if type(e) in my_excs:
#         print("yup")
#     else:
#         print("nope")

# if MyException in my_excs:
#     print("yes")
# else:
#     print("no")

# try:
#     raise MyException("Fuck me")
# except Exception as e:
#     raise type(e)(f"No really: {str(e)}")

raise MySecondException("okay")