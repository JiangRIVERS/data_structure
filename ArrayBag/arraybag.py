"""
File:arraybag.py

"""
import math
from ArrayBag.arrays import Array

class ArrayBag(object):
    """An array-based bag implementation"""
    #DEFAULT_CAPCITY=10

    #Constuctor
    def __init__(self,DEFAULT_CAPCITY=10,sourceCollection=None):
        """Sets the initial state of self,
        which includes the contents of source Collection,if it's present"""
        self.DEFAULT_CAPCITY=DEFAULT_CAPCITY
        self._items=Array(self.DEFAULT_CAPCITY)
        self._size=0
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)



    #Accessor methods
    def isEmpty(self):
        """Returns True if len(self)==0,or False otherwise"""
        return len(self)==0

    def __len__(self):
        """Returns the number of items in self"""
        return self._size

    #Mutator methods
    def clear(self):
        """Makes self become empty"""
        self._size=0
        self._items=Array(self.DEFAULT_CAPCITY)

    def add(self,item):
        """Adds item to self"""
        if self._size==self.DEFAULT_CAPCITY:
            self.DEFAULT_CAPCITY+=1
        self[len(self)]=item
        self._size+=1

    def __iter__(self):
        """Support iteration over a view of self.Unlike arrays.py.__iter__,do not show 'none' in arrays"""
        cursor=0
        while cursor<len(self):
            yield self[cursor]
            cursor+=1

    def __str__(self):
        '''Returns the string representation of self'''
        return "{"+",".join(map(str,self))+"}"

    def __add__(self, other):
        """Returns a new bag containing the content of self and other"""
        result=self#创建self的副本
        for item in other:
            result.add(item)
        return result

    def __eq__(self, other):
        """Returns True if self equals other or False otherwise"""
        if self is other:return True
        if type(self)!=type(other) or \
            len(self)!=len(other):
            return False
        for item in self:
            if item not in other:
                return False
        return True

    def __getitem__(self,index):
        """Subscript operator for access at index"""
        return self._items[index]

    def __setitem__(self,index,newItem):
        """Subscript operator for replacement at index"""
        self._items[index]=newItem

    def remove(self,item):
        """
        postcondition:item is removed from self
        1.check the postcondition ,if it's not satisfied,throw an Keyerror
        2.searching the Array for the target
        3.move the rest and the logical size of the Array should be reduced
        4.adjust the Array's physical size if necessary
        """
        #check postcondition and raise if necessary
        if item not in self:
            raise KeyError(str(item)+"not in bag")
        #search for index of target item
        targetIndex=0
        for targetItem in self:
            if targetItem==item:
                break
            targetIndex+=1

        #Shift items to the left of target up by one position
        for i in range(targetIndex,len(self)-1):
            self[i]=self[i+1]
        #Decrement logical size
        self._size-=1
        #Check array momory here and decrease it if necessary
        if self._size<=1/4*self.DEFAULT_CAPCITY:
            temp=ArrayBag(math.ceil(self.DEFAULT_CAPCITY//2))
            for i in range(len(self)):
                temp[i]=self._items[i]









