class dect:
    def __init__(self, func):
        self.__func = func

    @property
    def func(self):
        return self.__func

    @func.setter
    def func(self, func):
         func = self.__func
         return func


    @func.deleter
    def func(self):
        print("Deleting function...")
        del self.__func



d1 = dect(lambda x: x + 1)
print(d1.func(5)) # This will call the lambda function and return 6

del d1.func # This will delete the function and print "Deleting function..."