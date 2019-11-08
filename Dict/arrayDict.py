"""
Filename:arraydict.py
"""

from Dict.abstractdict import AbstractDict
from Dict.Item import Item

class ArrayDict(AbstractDict):
    """Represents an array-based dictionary"""

    def __init__(self,sourceCollection=None):
        """Will copy items to the collection
        from sourceCollection if it's present"""
        self._item=list()
        AbstractDict.__init__(self,sourceCollection)

    #Accessors
    def _index(self,key):
        """Helper method for key search"""
        index=0
        for item in self._item:
            if item.key==key:
                return index
            index+=1
        return -1

    def __setitem__(self, key, value):
        """If the key is not in the dictionary,
        adds the key and value to it
        Otherwise, replaces the old value with the
        new value."""
        index=self._index(key)
        if index==-1:
            self._item.append(Item(key,value))
            self._size+=1
        else:
            self._item[index].value=value

    def __getitem__(self, key):
        """Precondition: the key is in the dictionary.
        Raises a KeyError if the key is not in the
        dictionary.
        Returns the value associated with the key."""
        index=self._index(key)
        if index==-1:
            raise KeyError("Missing key:"+str(key))
        return self._item[index].value


    def __iter__(self):
        """Serves up the keys in the dictionary"""
        cursor=0
        while cursor<len(self):
            yield self._item[cursor].key
            cursor+=1

    def pop(self,key):
        """Precondition: the key is in the dictionary.
        Raises a KeyError if the key is not in the dictionary.
        Removes the key and returns the associated value
        if the key is in the dictionary, or returns the
        default value otherwise."""
        index=self._index(key)
        if index==-1:
            raise KeyError("Missing key:"+str(key))
        self._size-=1
        return self._item.pop(index).value
