#single inheritance
class whatsappv1:
    def message(self):
        print("you can send message ")

class whatsappv2(whatsappv1):
    def status(self):
        print("you can upload a status for 24hrs")


msg = whatsappv1()
msg.message()


st = whatsappv2()
st.status()
st.message()

#multi-level inheritance

class whatsappv1:
    def message(self):
        print("you can send message ")

class whatsappv2(whatsappv1):
    def status(self):
        print("you can upload a status for 24hrs")

class whatsappv3(whatsappv2):
    def group(self):
        print("you can crate group ")


msg = whatsappv1()
msg.message()


st = whatsappv2()
st.message()
st.status()

grp = whatsappv3()
grp.message()
grp.status()
grp.group()


#multiple Inheritance

class whatsappv1:
    def message(self):
        print("you can send message ")

class whatsappv2(whatsappv1):
    def status(self):
        print("you can upload a status for 24hrs")

class whatsappv3:
    def group(self):
        print("you can crate group ")


class whatsappv4:
    def community(self):
        print("ypu can join in a community")

class whatsappv5(whatsappv4,whatsappv3,whatsappv2):
    def channels(self):
        print("You join in a channels")


v5= whatsappv5()
v5.message()
v5.status()
v5.group()
v5.community()
v5.channels()  

class whatsappv1:
    def message(self):
        print("you can send message ")

class whatsappv2(whatsappv1):
    def status(self):
        print("you can upload a status for 24hrs")

class whatsappv3(whatsappv1):
    def group(self):
        print("you can crate group ")


class whatsappv4(whatsappv1):
    def community(self):
        print("ypu can join in a community")

class whatsappv5(whatsappv1):
    def channels(self):
        print("You join in a channels")

v1 = whatsappv2()
v1.message()
v1.status()

