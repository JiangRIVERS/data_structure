"""
Filename:AbstractCollection.py
The ultimate class.Other son classes can inherit its method.
Method:_size、isEmpty、__len__、__str__、__add__、__eq__.
"""
class AbstractCollection(object):

    def __init__(self,sourceCollection=None):
        self._size=0
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)

    def isEmpty(self):
        return len(self)==0

    def __len__(self):
        return self._size

    def __str__(self):
        return "{"+",".join(map(str,self))+"}"

    def __add__(self, other):
        result=self
        for item in other:
            result.add(item)
        return result

    def __eq__(self, other):
        if self is other:return True#(type(self))==char or number,a is b euqals to a==b
        if type(self)!=type(other) or \
            len(self)!=len(other):
            return False
        for item in self:
            if item not in other:
                return False
        return True



