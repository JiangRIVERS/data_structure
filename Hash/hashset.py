"""
Filename:hashset.py

A set implementation based on hash function
"""

from LinkedBag.linked_structure import Node
from ArrayBag.arrays import Array
from Set.AbstractSet import AbstractSet
from AbstractCollection import AbstractCollection

class HashSet(AbstractCollection,AbstractSet):
    """A hashing implementation of a set."""

    DEFAULT_CAPACITY=3
    def __init__(self,sourceCollection=None,capacity=None):

        if capacity==None:
            self._capacity=HashSet.DEFAULT_CAPACITY
        else:
            self._capacity=capacity
        self._item=Array(self._capacity)
        self._foundNode=self._priorNode=None
        self._index=-1
        AbstractCollection.__init__(self,sourceCollection)

    # Accessor methods
    def __contains__(self, item):
        """Returns True if item is in the set or
        False otherwise."""
        self._index=abs(hash(item))%len(self._item)
        self._priorNode=None
        self._foundNode=self._item[self._index]
        while self._foundNode!=None:
            if self._foundNode.data==item:
                return True
            else:
                self._priorNode=self._foundNode
                self._foundNode=self._foundNode.next
        return False

    def __iter__(self):
        """Supports iteration over a view of self."""
        if self.isEmpty():
            raise KeyError("The set is empty.")

        else:
            for index in range(len(self._item)):
                self._priorNode=None
                self._foundNode=self._item[index]
                while self._foundNode!=None:
                    yield self._foundNode.data
                    self._priorNode=self._foundNode
                    self._foundNode=self._foundNode.next

    def __str__(self):
        """Returns the string representation of self."""
        if self.isEmpty():
            return None
        else:
            for index in range(len(self._item)):
                list = []
                self._priorNode=None
                self._foundNode=self._item[index]
                while self._foundNode!=None:
                    list.append(self._foundNode.data)
                    self._priorNode=self._foundNode
                    self._foundNode=self._foundNode.next
                print(str(index)+":"+"-->".join(map(str,list)))
        return "string of set is shown above"

    #Mutator methods
    def clear(self):
        """Makes self become empty."""
        self._size=0
        self._item=Array(HashSet.DEFAULT_CAPACITY)

    def add(self,item):
        """Adds item to the set if it is not in the set."""
        if not item in self:
            newNode=Node(item,self._item[self._index])
            self._item[self._index]=newNode
            self._size+=1

    def remove(self,item):
        if not item in self:
            raise KeyError(str(item)+"is not in the set.")
        else:
            if self._priorNode==None:
                self._item[self._index]=None
            else:
                self._priorNode.next=self._foundNode.next




