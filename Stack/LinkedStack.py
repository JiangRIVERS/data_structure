"""
Filename:LinkedStack.py
Create a linedbased stack
"""
from LinkedBag.linked_structure import Node
from AbstractCollection import AbstractCollection

class LinkedStack(AbstractCollection):
    """Link-based stack implement"""

    def __init__(self,sourceCollection=None):
        self._item=None
        AbstractCollection.__init__(self,sourceCollection)

    #Accessors
    def __iter__(self):
        def visitNodes(node):
            """Visit the stack from bottom to top"""
            if not node is None:
                visitNodes(node.next)
                tempList.append(node.data)
        tempList=[]
        visitNodes(self._item)
        return iter(tempList)

    def peek(self):
        """Returns the item at top of the stack
        Precondition:the stack is not empty
        Raises KeyError if the stack is empty"""
        if self.isEmpty():
            raise KeyError("the stack is empty")
        return self._item.data

    #Mutators
    def clear(self):
        self._size=0
        self._item=None

    def push(self,item):
        self._item=Node(item,self._item)
        self._size+=1

    def pop(self):
        """Removes and returns the item at the top of the stack
        Precondition:stack is empty
        Raise:KeyError if the stack is empty"""
        if self.isEmpty():
            raise KeyError("the stack is empty")
        result=self._item.data
        self._size-=1
        self._item=self._item.next
        return result






