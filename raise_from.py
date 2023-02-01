class CustomException(Exception):
    pass


def test_func():
    return 1 / 0


try:
    test_func()
except Exception as e:
    pass
    raise CustomException("raising custom error")
