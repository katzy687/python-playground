from pydantic import BaseModel
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from dataclasses import dataclass as basemodel_decorator
else:
    def basemodel_decorator(func):
        return func


class SandboxApiBaseModel(BaseModel):
    """ Base Model for all other classes. Defines useful helper methods """

    class Config:
        use_enum_values = True

    response_dict: dict = None
    """ this attribute will cache the original response before loading into model """


@basemodel_decorator
class BlueprintDescription(SandboxApiBaseModel):
    id: Optional[str]
    name: Optional[str]

@basemodel_decorator
class ExtendedDescription(BlueprintDescription):
    fuck: str


a = BlueprintDescription(id="99", name="haha")
x = ExtendedDescription(fuck="you", **a.dict())
print(x.json())