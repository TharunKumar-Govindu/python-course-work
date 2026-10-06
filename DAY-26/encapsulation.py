class Instagram:
    def __init__(self,username,password):
        self.username = username
        self.__password = password
        self._post = []


    def getpassword(self):
        return self.__password


    def setpassword(self,newpassword):
        self.__password = newpassword


    @property
    def accesspost(self):
        return self._post


    @accesspost.setter
    def accesspost(self,newpost):
        self._post.append(newpost)


info =Instagram('tharun',123244)

print(info.username)
print(info.getpassword())
print(info.accesspost)

info.username ='tharun_22'
print(info.username)

info.setpassword('tharun00998')
print(info.getpassword())


info.accesspost ='python'
info.accesspost ='java'
print(info.accesspost)
