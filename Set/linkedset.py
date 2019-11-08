"""
Filename:linkedset.py
"""

from LinkedBag.linkedbag import LinkedBag
from Set.AbstractSet import AbstractSet

class ArraySet(LinkedBag,AbstractSet):
    """An linked-based implementation of a set"""

    def __init__(self,sourceCollection=None):
        LinkedBag.__init__(self,sourceCollection)

    def add(self,item):
        """Adds item to the set if it is not in the set"""
        if not item in self:
            LinkedBag.add(self,item)
