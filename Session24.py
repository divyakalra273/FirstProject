class Point:

    def __init__(self,x,y):
        self.x=x
        self.y=y

    def showPoint(self):
        print("{} | {} ".format(self.x,self.y))

    def __str__(self):
        print("{} | {} ".format(self.x, self.y))

p1=Point(10,20)

print(p1)
print(p1.__str__())

