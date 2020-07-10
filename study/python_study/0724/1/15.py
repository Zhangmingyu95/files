__author__ = 'mingyu.zhang'
from enum import Enum

class Month(Enum):
    JAN = 1
    FEB=2
    MAR=3
    MAR_ALIAS=3

print(Month.FEB)
print(Month.FEB.name)
print(Month.FEB.value)
print(Month.__members__.items())
print(type(Month.FEB))