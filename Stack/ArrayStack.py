"""
Filename:ArrayStack.py
Create an array implement of stack
"""
from ArrayBag.arrays import Array
from AbstractCollection import AbstractCollection
import math

class ArrayStack(AbstractCollection):
    """An array-based stack implement"""

    def __init__(self,DEFAULT_CAPCITY=10,sourceCollection=None):
        self.DEFAULT_CAPCITY=DEFAULT_CAPCITY
        self._items=Array(DEFAULT_CAPCITY)
        AbstractCollection.__init__(self,sourceCollection)

    def add(self,item):
        if len(self)==self.DEFAULT_CAPCITY:
            self.DEFAULT_CAPCITY+=1
        self._items[len(self)]=item
        self._size += 1

    #Accessors
    def __iter__(self):
        """Supports iterration over a view of self.
        Visits items from bottom to top of stack"""
        cursor=0
        while cursor<len(self):
            yield self._items[cursor]
            cursor+=1

    def peek(self):
        """Returns the item at top of the stack
        Precondition:the stack is not empty
        Raises KeyError if the stack is empty"""
        if self.isEmpty():
            raise KeyError("the stack is empty")
        return self._items[len(self)-1]

    #Mutators
    def clear(self):
        self._size=0
        self._items=Array(self.DEFAULT_CAPCITY)

    def push(self,item):
        """
        Inserts item at top of the stack
        Precondition:The stack is full
        Raise KeyError if the stack is full
        Postcondition:add item to the top of the stack
        """
        if len(self)==self.DEFAULT_CAPCITY:
            raise KeyError("the stack is full")
        self.add(item)

    def pop(self):
        """
        Removes and returns the item at the top of the stack
        Precondition:the stack is not empty
        Raise KeyError if the stack is empty
        Postcondition:the top item is removed from the stack
        """
        if self.isEmpty():
            raise KeyError("the stack is empty")
        result=self._items[len(self)-1]
        self._items[len(self)-1]=None
        self._size-=1
        if len(self)<=1/4*self.DEFAULT_CAPCITY:
            temp=Array(math.ceil(self.DEFAULT_CAPCITY//2))
            for i in range(len(self)):
                temp[i]=self._items[i]
        return result




