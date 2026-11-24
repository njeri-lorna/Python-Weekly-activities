from abc import ABC, abstractmethod

# Abstract class
class Payment(ABC):

    @abstractmethod
    def makePayment(self):
        pass


# Child class 1
class MobileMoneyPayment(Payment):

    def makePayment(self):
        print("Payment made using Mobile Money")


# Child class 2
class CardPayment(Payment):

    def makePayment(self):
        print("Payment made using Bank Card")


# Main program
payment1 = MobileMoneyPayment()
payment2 = CardPayment()

payment1.makePayment()
payment2.makePayment()
