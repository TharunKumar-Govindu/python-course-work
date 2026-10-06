class Redbus:
    bus = {i:"Available" for i in range(1,11)}

    def dispalyseats(self):
        print("-----xyz-----")
        for i in Redbus.bus:
            print(i,Redbus.bus[i])

    def booking(self,seatno):
        for i in Redbus.bus:
            if i==seatno and Redbus.bus[i]=='Avialable':
                Redbus.bus[i]="Booked"
class User(Redbus):
    def __init__(self,name,email,phno):
        self.name=name
        self.email=email            