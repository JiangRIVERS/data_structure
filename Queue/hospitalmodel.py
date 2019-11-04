"""
Filename:hospitalmodel.py
"""
from Queue.linkedpriorityqueue import Comparable
from Queue.linkedpriorityqueue import LinkedPriorityQueue

class Condition(object):

    def __init__(self,rank):
        self._rank=rank

    def __str__(self):
        if self._rank==1:return "critical"
        elif self._rank==2:return "serious"
        else:return "fair"

class Patient(Comparable):

    def __init__(self,name,condition):
        self._name=name
        self._condition=str(condition)
        Comparable.__init__(self,name,condition._rank)

    def __str__(self):
        return self._name+" / "+self._condition

class ERModel(LinkedPriorityQueue):

    def __init__(self,sourceCollection=None):
        LinkedPriorityQueue.__init__(self,sourceCollection)


