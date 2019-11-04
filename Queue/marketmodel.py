"""
Filename:marketmodel.py
"""

from Queue.cashier import Cashier
from Queue.customer import Customer

class MarketModel(object):

    def __init__(self,lengthOfSimulation,averageTimePerCus,probabilityofNewArrival):
        self._probabilityofNewArrival=probabilityofNewArrival
        self._lengthOfSimulation=lengthOfSimulation
        self._averageTimePerCus=averageTimePerCus
        self._cashier=Cashier()

    def runSimulation(self):
        for currentTime in range(self._lengthOfSimulation):
            customer=Customer.generateCustomer(self._probabilityofNewArrival,currentTime,self._averageTimePerCus)

            if customer!=None:
                self._cashier.addCustomer(customer)
            self._cashier.serveCustomers(currentTime)

    def __str__(self):
        return str(self._cashier)

if __name__=="__main__":
    market=MarketModel(int(input("lengthOfSimulation:")),int(input("averageTimePerCus:")),
                       float(input("probabilityofNewArrival:")))
    market.runSimulation()
    print("--------------------")
    print(str(market))
