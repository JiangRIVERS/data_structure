"""
Filename:hashdict.py

A dict implementation based on hash function
"""
from Dict.abstractdict import AbstractDict
from Dict.Item import Item
from LinkedBag.linked_structure import Node
from ArrayBag.arrays import Array

class HashDict(AbstractDict):
    """Representa a hash-based dictionary."""

    DEFAULT_CAPACITY=9

    def __init__(self,sourceCollection=None):
        """Will copy items to the collection from
        sourceCollection if it's present."""
        self._array=Array(HashDict.DEFAULT_CAPACITY)
        self._foundNode=self._priorNode=None
        self._index=-1
        AbstractDict.__init__(self,sourceCollection)

    #Accessors
    def __contains__(self, key):
        """Returns True if key is in self
        of False otherwise."""
        self._index=abs(hash(key))%len(self._array)
        self._priorNode=None
        self._foundNode=self._array[self._index]
        while self._foundNode!=None:
            if self._foundNode.data.key==key:
                return True
            else:
                self._priorNode=self._foundNode
                self._foundNode=self._foundNode.next()
        return False

    def __iter__(self):
        """Servers up the keys in the dictionary"""
        if self.isEmpty():
            raise KeyError("The dict is empty.")
        else:
            for index in range(len(self._array)):
                self._priorNode=None
                self._foundNode=self._array[index]
                while self._foundNode!=None:
                    yield self._foundNode.data.key
                    self._priorNode=self._foundNode
                    self._foundNode=self._foundNode.next

    def __getitem__(self, key):
        """Precondition: the key is in the dictionary.
        Raises: a KeyError if the key is not in the
        dictionary.
        Returns the value associated with the key."""
        if key in self:
            return self._foundNode.data.value
        else:
            raise KeyError("Missing: "+str(key))

    #Mutators
    def __setitem__(self, key, value):
        """If the key is in the dictionary,
        replaces the old value with the new value.
        Otherwise, adds the key and value to it."""
        if key in self:
            self._foundNode.data.value=value
        else:
            newNode=Node(Item(key,value),self._array[self._index])
            self._array[self._index]=newNode
            self._size+=1

    def pop(self,key):
        """Removes the key and returns the associated valye
        if the key in the dictionary, or returns the
        default value otherwise."""
        if not key in self:
            raise KeyError("Missing: "+str(key))
        elif self._priorNode==None:
            self._array[self._index]=self._foundNode.next
        else:
            self._priorNode.next=self._foundNode.next
        self._size-=1
        return self._foundNode.data.value


