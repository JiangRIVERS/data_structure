"""
Filename:LinkedQueue.py
Create a Queue class base on Linked_Structure
"""
from LinkedBag.linked_structure import Node
from AbstractCollection import AbstractCollection

class LinkedQueue(AbstractCollection):

    def __init__(self,sourceCollection=None):
        self._front=self._rear=None
        AbstractCollection.__init__(self,sourceCollection)

    def __iter__(self):
        cursor=self._front
        while not cursor is None:
            yield cursor.data
            cursor=cursor.next

    def __contains__(self, item):
        for i in self:
            if i==item:
                return True
            else: return False

    def add(self,newItem):
        newNode=Node(newItem,None)
        if self.isEmpty():
            self._front=newNode
        else:
            self._rear.next=newNode
        self._rear=newNode
        self._size+=1

    def pop(self):
        if self.isEmpty():
            raise KeyError("The queue is empty")
        else:
            oldItem=self._front.data
            self._front=self._front.next
            if self._front is None:
                self._rear=None
            self._size-=1
            return oldItem

    def clear(self):
        self._size=0
        self._front=self._rear=None



