"""
https://github.com/lidatong/dataclasses-json
"""
import json
from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class Person:
    name: str


person = Person(name='lidatong')
json_sample = person.to_json()  # '{"name": "lidatong"}' <- this is a string
dict_sample = person.to_dict()  # {'name': 'lidatong'} <- this is a dict
loaded_from_json = Person.from_json(json_sample)  # Person(1)
loaded_from_dict = Person.from_dict(dict_sample)
pretty_json = json.dumps(dict_sample, indent=4)# Person(1)
pass