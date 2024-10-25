# class Teddy:
#     quantity=200
# teddy1=Teddy()
# teddy2=Teddy()
# print(teddy1.quantity)
# print(teddy2.quantity)
class student:
    def __init__(self,name,mark):
        self.name=name
        self.mark=mark
    def getdetails(self):
        self.name=input("enter your name")
        self.mark=int(input("enter your mark"))
    def putdetails(self):
        print("dear ",self.name,", your mark is",self.mark)
obj=student("","")
obj.getdetails()
obj.putdetails()