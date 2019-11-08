"""
Filename:arrayset.py
"""

from ArrayBag.arraybag import ArrayBag
from Set.AbstractSet import AbstractSet

class ArraySet(ArrayBag,AbstractSet):
    """An array-based implementation of a set"""

    def __init__(self,DEFAULT_CAPCITY=10,sourceCollection=None):
        ArrayBag.__init__(self,DEFAULT_CAPCITY,sourceCollection)

    def add(self,item):
        """Adds item to the set if it is not in the set"""
        if not item in self:
            ArrayBag.add(self,item)

