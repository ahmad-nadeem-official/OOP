from abc import ABC, abstractmethod

class main(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def salary(self, amount):
        pass    

    def intro(self):
        print(f"my name is {self.name}")

class manager(main):
        
    def salary(self, amount):
        print(f"my salary is {amount}")

class dev(main):
    
    def salary(self, amount):
        print(f"my salary is {amount}")        

objects = [
    manager("ahmad"), dev("ali")
    ]

for obj in objects:
    obj.intro()
    obj.salary(10000)