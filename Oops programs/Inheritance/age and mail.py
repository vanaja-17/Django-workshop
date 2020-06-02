class Person:
    def __init__(self,age,mailid):
        self.age=age
        self.mailid=mailid
    def getage(self):
        return self.age
    def getmailid(self):
        return self.mailid
#child class
class Emp(Person):
    def data():
        obj=Person(12,"vanaja@gmail.com")
        print(obj.getage())

o=Emp()
o.data()
