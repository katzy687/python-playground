from dataclasses import dataclass, asdict


@dataclass
class Seeds:
    color: str


@dataclass
class Fruits:
    apple: str
    seeds: Seeds


@dataclass
class Vegetables:
    eggplant: str


@dataclass
class Config:
    fruit_container: Fruits
    veggie_box: Vegetables


config = Config(Fruits("red delicious", Seeds("black")), Vegetables("purple"))
x = asdict(config)
pass
