"""
Filename:linkedpriorityqueue.py
A link-based priority queue.
Comparable class is utilized for the object that cannot be compared directly.
"""

from LinkedBag.linked_structure import Node
from Queue.LinkedQueue import LinkedQueue

class Comparable(object):
    """Wrapper class for items that are not comparable"""

    def __init__(self,data,priority=1):
        self._data=data
        self._priority=priority

    def __str__(self):
        """Returns the string rep of the contained datum"""
        return str(self._data)

    def __eq__(self, other):
        """Returns True if the contained priorities are equal
        or False otherwise"""
        if self is other:return True
        if type(self)!=type(other):return False
        return self._priority==other.getPriority()

    def __lt__(self, other):
        """Returns True if self's priority < other's priority or False otherwise"""
        return self._priority<other.getPriority()

    def __le__(self, other):
        """Returns True if self's priority <= other's priority or False otherwise"""
        return self._priority<=other.getPriority()

    def getData(self):
        """Returns the contained datum"""
        return self._data

    def getPriority(self):
        """Returns the contained priority"""
        return self._priority


class LinkedPriorityQueue(LinkedQueue):
    """A link-based priority queque implementation"""

    def __init__(self, sourceCollection=None):
        LinkedQueue.__init__(self, sourceCollection)

    def add(self, newItem):
        if self.isEmpty() or newItem >= self._rear.data:
            #New item goes at rear
            LinkedQueue.add(self,newItem)

        else:
            #Search for a position where it's a less
            probe=self._front
            while probe.data<=newItem:
                trailer=probe
                probe=probe.next

            newNode=Node(newItem,probe)
            if probe==self._front:
                self._front=newNode
            else:
                trailer.next=newNode

            self._size+=1


