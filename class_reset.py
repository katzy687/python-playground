import dataclasses


@dataclasses.dataclass
class Test:
    a: str
    b: str

    def refresh_instance(self):
        self.__dict__["fuck"] = "you"


x = Test("a_val", "b_val")
x.refresh_instance()
print(x.__dict__)

