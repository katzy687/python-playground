from abc import ABC, abstractmethod


class MyBase(ABC):

    @abstractmethod
    def __init__(self, x):
        self.x = x

    def lollers(self):
        raise NotImplementedError


class RealClass(MyBase):
    def __init__(self, x):
        super().__init__(x)


thing = RealClass("lol")
print(thing.lollers())