"""
Filename:customer.py
"""

import random

class Customer(object):

    @classmethod#类方法
    def generateCustomer(cls,probabilityofNewArrival,arrivalTime,averageTimePerCustomer):
        if random.random()<=probabilityofNewArrival:
            return Customer(arrivalTime,averageTimePerCustomer)
        else:return None

    def __init__(self,arrivalTime,serviceNeeded):
        self._arrivalTime=arrivalTime
        self._amountOfServiceNeeded=serviceNeeded

    def arrivalTime(self):
        return self._arrivalTime

    def amountOfServiceNeeded(self):
        return self._amountOfServiceNeeded

    def serve(self):
        self._amountOfServiceNeeded-=1