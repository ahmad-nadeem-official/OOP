# here we will talk about constructors

class bank_acc:
    def __init__(self):
        self.acc_holder = "unknown"
        self.balance = 0
        self.acc_type = "saving"
        print(f"account holder is {self.acc_holder} and his balance is {self.balance} and his account type is {self.acc_type}") 

class new_bank_acc:
    def __init__(self, acc_holder, balance, acc_type):
        self.acc_holder = acc_holder
        self.balance = balance
        self.acc_type = acc_type
        print(f"A new account has been created for {self.acc_holder} and his balance is {self.balance} and his account type is {self.acc_type}") 

class premium_bank_acc(bank_acc):
    def __init__(self, reward_points):
        super().__init__()
        self.reward_points = reward_points        
        print(f"Premium benefits activated with {self.reward_points} reward points!")

def main():
    while True:
        print("\n--- Menu ---")
        print("1. Create a new bank account")
        print("2. Create a premium bank account")
        print("3. Fully customized account")
        print("(Type 'exit' at any prompt to quit)")

        usr_name = input("Enter Account holder name: ")
        balance = input("Enter Account balance: ")
        acc_type = input("Enter Account type: ")
        reward_points = input("Enter reward points: ")

        # 1. MOVE EXIT CHECK TO THE VERY TOP
        if "exit" in [usr_name.lower(), balance.lower(), acc_type.lower(), reward_points.lower()]:
            print("Exiting...")
            break

        # 2. Process conditions normally now that exit is handled
        if usr_name == "" and balance == "" and acc_type == "" and reward_points == "":
            print("kindly wait working now...")
            deflt = bank_acc()

        elif usr_name and balance == "" and acc_type == "" and reward_points == "":
            deflt1 = bank_acc()

        elif usr_name and balance and acc_type == "" and reward_points == "":
            deflt2 = bank_acc()

        elif usr_name and balance and acc_type and reward_points == "":
            deflt3 = new_bank_acc(usr_name, balance, acc_type)

        elif usr_name and balance and acc_type and reward_points:
            deflt4 = premium_bank_acc(reward_points)

main()             
