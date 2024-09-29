"""CQ04 - imports and calls concat from concatonation"""

__author__ = "730752527"

from CQs.cq04.concatenation import concat
from CQs.cq04.coordinates import get_coords


x: str = "123"
y: str = "abc"

print(concat(str1=x, str2=y))
get_coords(x, y)
