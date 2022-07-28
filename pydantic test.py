import json
from enum import Enum
from typing import TYPE_CHECKING, Optional
from pydantic import BaseModel, Field

if TYPE_CHECKING:
    from dataclasses import dataclass as _basemodel_decorator
else:
    _basemodel_decorator = lambda x: x

@_basemodel_decorator
class CustomBaseModel(BaseModel):
    def pretty_json(self, indent=4):
        return self.json(indent=indent)


@_basemodel_decorator
class User(CustomBaseModel):
    name: str
    age: Optional[int]
    """ age is required """


# class UserWithDetails(User):
#     kinks: str
response = '{"name": "natti", "age":"11"}'
x = User.(name="natti", age=9)
User.config.
print(x)