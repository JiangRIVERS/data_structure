"""
File:arrays.py

An Arrays is like a list,but the client can use only [],len,iter,and str.

To instantiate,use

<Variable>=Array(<capacity>,<optional fill value>)

The file value is None by default
"""

class Array(object):
    """Represents an array"""

    def __init__(self,capcity,fillValue=None):
        """Capcity is the static size of the array.
        fillValue is placed at each position."""
        self._items=list()
        for count in range(capcity):
            self._items.append(fillValue)

    def __len__(self):
        """The capacity of the array."""
        return len(self._items)

    def __str__(self):
        """The string representation of the array."""
        return str(self._items)

    def __iter__(self):
        """Supprts traversal withe a for loop"""
        return iter(self._items)

    def __getitem__(self,index):
        """Subscript operator for access at index"""
        return self._items[index]

    def __setitem__(self,index,newItem):
        """Subscript operator for replacement at index"""
        self._items[index]=newItem

