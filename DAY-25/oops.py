class Flipkart:
    discount = 30

    @classmethod
    def updatediscount(cls):
        cls.discount = 40
        print("Updated Discount:", cls.discount)

        
    def info(self,name,phoneno,address):
        self.name = name
        self.phoneno = phoneno
        self.adddress = address
        print('Welcome to Flipkart ',self.name)

    @staticmethod
    def banner():
        print(f"{Flipkart.discount}% discount is going ,grab it")

narayana = Flipkart()
narayana.info('narayana',123456789,'AP')
narayana.updatediscount()
narayana.banner()

alluarjun = Flipkart()
alluarjun.info('alluarjun',123456789,'kmply')
alluarjun.updatediscount()
alluarjun.banner()

tharun = Flipkart()
tharun.info('tharun',123456789,'hyd')
tharun.updatediscount()
tharun.banner()






  