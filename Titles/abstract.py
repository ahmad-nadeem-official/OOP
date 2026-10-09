from abc import ABC, abstractmethod

class main(ABC):
    @abstractmethod
    def sound(self):
        pass

class sports_car(main):
    def sound(self):
        print("vimmmmmmmmmmmm")   

class suv_car(main):
    def sound(self):
        print("gimmmmmmmmmmmm")


def runner(obj):
    obj.sound()


objects = [
    sports_car(), suv_car()
    ]

for obj in objects :
    runner(obj)


         
