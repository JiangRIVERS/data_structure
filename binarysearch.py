"""
Filename:binarysearch.py
implement a binarysearch
O(n)=O(logn)
precondition:The list to be searched should be sorteed
"""
def binarysearch(target,sortedLyst):
    left=0
    right=len(sortedLyst)-1
    while left<=right:
        midpoint=(left+right)//2
        if sortedLyst[midpoint]==target:
            return True
        elif sortedLyst[midpoint]<=target:
            left=midpoint+1
        else:
            right=midpoint-1
    return False