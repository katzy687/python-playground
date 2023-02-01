from pydantic import BaseModel
from typing import TYPE_CHECKING, List, Optional
from pydantic import parse_obj_as

# added for dev intellisense: https://stackoverflow.com/a/71257588
if TYPE_CHECKING:
    from dataclasses import dataclass as _basemodel_decorator
else:
    def _basemodel_decorator(func):
        return func


@_basemodel_decorator
class MyModel(BaseModel):
    val1: str = "lol"
    val2: int = 5


@_basemodel_decorator
class DataList(BaseModel):
    data: List[MyModel]


data = {"val1": "yo", "val2": 9}
x = MyModel().parse_obj(data)
data_list = [data]
y = parse_obj_as(List[MyModel], data_list)
print(len(y))