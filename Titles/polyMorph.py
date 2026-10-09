class rectangle :
    def __init__(self, leng, wid):
        self.leng = leng
        self.wid = wid

    def area(self) -> int:
        return self.leng * self.wid


class square(rectangle):
    def __init__(self, leng, wid):
         super().__init__(leng,wid)

    def area(self) -> int:
            return self.leng * self.wid


class circle:
     def __init__(self, rad):
          self.rad = rad

     def area(self) -> float:
          return 3.14 * self.rad ** 2


class point:
     def __init__(self, x:int, y:int):
          self.x = x
          self.y = y

     def __add__(self, other):
          return point(
               self.x + other.x,
               self.y + other.y

          ) 
     def area(self) -> float:
          return self.x + self.y 


#####################duck typing####################
def show_area(obj):
     return obj.area()     
                   
rect = rectangle(50,10)
rect1 = rectangle(51,11)

cir = circle(5)
cir1 = circle(10)

sq = square(1,5)
sq1 = square(5,1)

pnt = point(5,10)
pnt1 = point(1,5)

objs = [rect,rect1, cir,cir1, sq,sq1, pnt,pnt1]

for obj in objs :
     print(show_area(obj))

print()

print("magic method by point")
p1 = point(1,6)
p2 = point(3,2)

p3 = p1 +p2
print(p3.x, p3.y)                     