from abc import ABC ,abstractmethod

class Payment(ABC):
    def source(self):
        print("Scanner/upiid/mobile number")
    def amount(self):
        print("Enter the amount ")
    def bank(self):
        print("Select the bank")
    def pin(self):
        print("Enter the pin")


    @abstractmethod
    def paymentprocess(self):
        pass
    def paymentstatus(self):
        print("Payment fail/success")

class HDFC(Payment):
    def paymentprocess(self):
        print("payment process theroug HDFC bank")

class ICIC(Payment):
    def paymentprocess(self):
        print("payment process through ICIC bank")

class UNION(Payment):
    def paymentprocess(self):
        print("payment process throug UNION bank")
class PBN(Payment):
    def paymentprocess(self):
        print("payment process throug PNB bank")



Nikhil = UNION()
Nikhil.source()
Nikhil.amount()
Nikhil.bank()
Nikhil.pin()
Nikhil.paymentprocess()
Nikhil.paymentstatus()