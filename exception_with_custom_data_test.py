class CustomDataException(Exception):
    def __init__(self, message, custom_data):
        Exception.__init__(self, message)
        super(CustomDataException, self).__init__(message)
        self.custom_data = custom_data


class DerivedClass(CustomDataException):
    def __init__(self, message, custom_data):
        super(DerivedClass, self).__init__(message, custom_data)


try:
    raise CustomDataException("this is some custom data", "this is some more data!")
except CustomDataException as e:
    print(e.message)
    print(e.custom_data)
    print(str(e))
