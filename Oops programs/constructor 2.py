class Mydata:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def mysum(self,c):
        return self.a+self.b+c
    def mymul(self):
        return self.a*self.b
a=int(input("Enter a value:"))
b=int(input("Enter b value:"))
o=Mydata(a,b)
c=int(input("Enter c value:"))
print(o.mysum(c))
print(o.mymul())
#o=Mydata(10,20)
#print(o.mysum(30))
