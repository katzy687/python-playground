from aenum import Constant
from enum import Enum


class MyConstants(Constant):
    TYPE_A = 'what the hell'
    TYPE_B = 'Another example'
    TYPE_C = 9


MyConstants.TYPE_C = 0