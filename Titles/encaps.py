class bank():

    def __init__(self, username, password):
        self.__username = username
        self.__password = password 
        self.__name = ""
        self.__acc_type = ""
        self.__balance = 0.0


    @property 
    def create_acc(self):
        return self.__name, self.__acc_type, self.__balance
            

    @create_acc.setter
    def create_acc(self, data):
        name, acc_type, balance = data
        self.__name = name
        self.__acc_type = acc_type
        self.__balance = balance

    def display(self, usrname, pswd):
        if self.__username == usrname and self.__password == pswd:
            print("Account Details:")
            print("Name:", self.__name)
            print("Account type", self.__acc_type)
            print("Balance:", self.__balance)
        else :
            print("Invalid username or password")    


# #user 1
# bank0 = bank("user123", "pass456")
# bank0.create_acc = ("Ahmad", "Business", 1000000000000000000000)
# bank0.display("user123", "pass456")

# #user 2
# bank1 = bank("user456", "pass789")
# bank1.create_acc = ("Ali", "Saving", 100000000000000000000)
# bank1.display("user456", "pass789")


# bank2 = bank("user789", "pass012")
# bank2.create_acc = ("Ayesha", "Current", 100000000000000000000)
# bank2.display("user789", "pass012")


print("simple getters and setters")

class bank1():
    
    def __init__(self, username, password):
        self.__username = username
        self.__password = password 
        self.__name = ""
        self.__acc_type = ""
        self.__balance = 0.0


    def create_acc(self):
        return self.__name, self.__acc_type, self.__balance


    def get_acc(self, data):
        name, acc, balance = data
        self.__name = name
        self.__acc_type = acc
        self.__balance = balance

    def display(self, usrname, pswd):
        if self.__username == usrname and self.__password == pswd:
            print("Account Details:")
            print("Name:", self.__name)
            print("Account type", self.__acc_type)
            print("Balance:", self.__balance)
        else :
            print("Invalid username or password")

# bank =  bank1("user123", "pass456")
# bank.get_acc(("Ahmad", "Business", 1000000000000000000000))
# bank.display("user123", "pass456")            