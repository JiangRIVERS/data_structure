"""
Filename:Grid.py
Returns a grid
"""
from ArrayBag.arrays import Array

class Grid(object):
    """Represents a two-dimensional array"""

    def __init__(self,rows,columns,fillValue=None):
        self._data=Array(rows)
        for row in range(rows):
            self._data[row]=Array(columns,fillValue)

    def getHeight(self):
        """Returns the number of rows"""
        return len(self._data)

    def getWidth(self):
        """Returns the number of colunmns"""
        return  len(self._data[0])

    def __getitem__(self,index):
        """Supports two-dimensional indexing with [row][column]"""
        return self._data[index[0]][index[1]]

    def __setitem__(self,index,newItem):
        self._data[index[0]][index[1]]=newItem


