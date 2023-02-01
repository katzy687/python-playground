from dataclasses import dataclass
import dacite

@dataclass
class Stuff:
    first: int
    second: int
    third: int


x = {"first": 1, "second": 2}
res = dacite.from_dict(Stuff, x, config=dacite.Config(str))
pass

