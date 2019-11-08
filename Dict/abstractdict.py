"""
Filename:abstractdict.py
"""
from AbstractCollection import AbstractCollection
from Dict.Item import Item

class AbstractDict(AbstractCollection):
    """Common data and method implementations for dictionaries
     You can consider self as a set of keys for comprehending easily."""

    def __init__(self,sourceColletion=None):
        """Will copy items to the collection
        from souceCollection if it's present"""
        AbstractCollection.__init__(self)
        if sourceColletion:
            #sourceCollection need to be a
            #key/value list, e.g., sourceCollection
            #=[('a',1)]
            if type(sourceColletion)==tuple:
                for key,value in [sourceColletion]:
                    self[key]=value
            else:
                sourcelist=[]
                for i in sourceColletion:
                    sourcelist.append(i)
                for key,value in sourcelist:
                    self[key]=value



    def items(self):
        """Returns an iterator on the items in
        the dictionary"""
        return map(lambda key:Item(key,self[key]),self)

    def __str__(self):
        return "{"+",".join(map(str,self.items()))+"}"

    def __add__(self, other):
        """Returns a new dictionary containing the
        contents of self and other"""
        result=type(self)(map(lambda item:(item.key,item.value),self.items()))
        result._size=self._size
        for key in other:
            result[key]=other[key]
        return result

    def keys(self):
        """Returns an iterator on the keys in
        the dictionary"""
        return iter(self)

    def values(self):
        """Returns a iterator on the values in
        the dictionary"""
        return map(lambda key:self[key],self)



