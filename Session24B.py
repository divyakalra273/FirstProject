class Point:

    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    def showPoint(self):
        print("{} | {}".format(self.x,self.y))

    def __str__(self):
        return "{} | {} | {}".format(self.x, self.y, hex(id(self)))

    def add(self,point):
        temp = Point()
        temp.x = self.x+point.x
        temp.y = self.y+point.y
        return temp

    def __add__(self,point):
        temp = Point()
        temp.x = self.x+point.x
        temp.y = self.y+point.y
        return temp

p1 = Point(10, 20)
p2 = Point(30,40)
p3 = Point()
p4 = Point()

p3 = p1.add(p2)
p4 = p1+p2

print(p3)
print(p4)
data = str(p1)
print(data)