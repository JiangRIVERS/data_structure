"""
Filename: Abstractset.py
"""

class AbstractSet(object):
    """
    Generic set method implementations:
    + __and__
      + s1 & s2
    + __or__
      + s1 | s2
    + __sub__
      + s1-s2
    + issubset
      + Judging whether s1 is the subset of s2.
    """
    def __or__(self, other):
        """Returns the union of self and other"""
        return self+other

    def __and__(self, other):
        """Returns the intersection of self and other"""
        intersection=type(self)()
        # create a variable and its type is same to self
        for item in self:
            if item in other:
                intersection.add(item)
        return intersection

    def __sub__(self, other):
        """Returns the difference of self and other"""
        difference=type(self)()
        for item in self:
            if not item in other:
                difference.add(item)
        return difference

    def issubset(self,other):
        """Returns True if self is a subset of other
        of False otherwise"""
        for item in self:
            if not item in other:
                return False
        return True
