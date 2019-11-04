"""
File:linkedbag.py
"""
from LinkedBag.linked_structure import Node

class LinkedBag(object):
    """A link-based bag impementation"""

    #Constructor
    def __init__(self,sourceCollection=None):
        """Sets the initial state of self,which includes the contents
        of sourceCollection,if it's present"""
        self._items=None#refers to external indicator
        self._size=0
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)

    def __iter__(self):
        """Supports iteration over a view of self"""
        cursor=self._items
        while cursor is not None:
            yield cursor.data
            cursor=cursor.next

    def clear(self):
        self._size=0
        self._items=None

    def add(self,item):
        """Adds item to self"""
        self._items=Node(item,self._items)
        self._size+=1

    def remove(self,item):
        """
        Precondition:item is in self
        Raises:KeyError if item is not in self
        postcondition:item is removed from self
        """
        #Check precondition and raise if necessary
        if item not in self:#allocate __contain__.If there is not __contain__,Python will generate 'for' method automatically.
            raise KeyError(str(item)+'not in bag')
        #Search for the node containing the target item
        #probe will point to the target node,and trailer
        #will point to the one before it,if it exists
        probe=self._items
        trailer=None
        for targetItem in self:
            if targetItem==item:
                break
            trailer=probe
            probe=probe.next
        #Unhook the node to be deleted,either the first one or the one thereafter
        if probe==self._items:
            self._items=self._items.next
        else:
            trailer.next=probe.next
        self._size-=1

