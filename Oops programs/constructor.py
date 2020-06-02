class Student:
    def __init__(self):
        print("HELLO!! I am constructor in class Student.")
class Demo:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def fun1(self):
        return self.a+self.b
Student()
o=Demo(10,22)
print(o.fun1())



    
