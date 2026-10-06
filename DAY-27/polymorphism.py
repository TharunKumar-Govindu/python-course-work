class Hotstar:
    def __init__(self,name):
        print(f"Welcome to Hotstar,{name}")
    def auth(self):
        print("You can lohin/register")
    def dashboard(self):
        print("You see the dashboaard")
    def search(self):
        print("You can search")
    def history(self):
        print("You can see the history")
    def palycontrol(self):
        print("play pause resume")
    def Ads(self):
        print("Ads will run")
    def quality(self):
        print("you have limited quality")
    def device(self):
        print("you single device")
    def access(self):
        print("Limited Access")
    def download(self):
        print("You cannot download")

class Primeium(Hotstar):
    def __init__(self,name):
        print(f"Welcome to Hotstar,{name}")
    def Ads(self):
        print("Ads will not run")
    def quality(self):
            print("you have high quality")
    def device(self):
        print("you can hautlipleve  device")
    def access(self):
        print("UnLimited Access")
    def download(self):
        print("You candown load")


nikhil = Hotstar('Nikhil')
nikhil.auth()
nikhil.dashboard()
nikhil.search()
nikhil.history()
nikhil.palycontrol()
nikhil.Ads()
nikhil.quality()
nikhil.access()
nikhil.device()
nikhil.download()

tharun = Primeium('Tharun')
tharun.auth()
tharun.dashboard()
tharun.search()
tharun.history()
tharun.palycontrol()
tharun.Ads()
tharun.quality()
tharun.access()
tharun.device()
tharun.download()

