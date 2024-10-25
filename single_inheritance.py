class Student:
    def __init__(self,name,mark):
        self.name=name
        self.mark=mark
    def getdetails(self):
        self.name=input("enter your name")
        self.mark=int(input("enter your mark"))
    def putd(self):
        print(self.name,self.mark)

class Teacher(Student):
    def display(self):
        print("you are excellent")

obj=Teacher("name","mark")
obj.getdetails()
obj.putd()
obj.display()