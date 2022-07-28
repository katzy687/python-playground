from typing import Type
from dataclasses import dataclass


@dataclass
class MyBaseError(Exception):
    f1: int
    f2: str

    def __str__(self):
        return f"got f1: {self.f1}, got f2: {self.f2}"


class ClientError(MyBaseError):
    pass


class AppClassBaseError(MyBaseError):
    pass



try:
    raise ClientError("fuck", "you")
except AppClassBaseError as e:
    print("gotcha")

