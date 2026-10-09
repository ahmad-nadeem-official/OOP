class bank_acc:
    def __init__(self):
        self.acc_holder = "unknown"
        self.balance = 0
        self.acc_type = "saving"


class premium_bank_acc(bank_acc):
    def __init__(self):
        self.reward_points = 0
        super().__init__()


def main():
    acc1 = bank_acc()
    print(f"account holder is {acc1.acc_holder} and his balance is {acc1.balance} and his account type is {acc1.acc_type}")

    acc2 = bank_acc()
    acc2.acc_holder = "ahmad"
    print(f"your balance is {acc2.balance} and account type is {acc2.acc_type}")

    acc3 = bank_acc()
    acc3.acc_holder = "jamshaid"
    acc2.balance = 1000
    print(f"account type is {acc3.acc_type}")

    acc4 = bank_acc()
    acc4.acc_holder = "ali"
    acc4.balance = 2000
    acc4.acc_type = "current"
    print(f"account holder is {acc4.acc_holder} and his balance is {acc4.balance} and his account type is {acc4.acc_type}")

    acc5 = premium_bank_acc()
    acc5.acc_holder = "ahmad"
    acc5.balance = 5000
    acc5.acc_type = "premium"
    acc5.reward_points = 100
    print(f"account holder is {acc5.acc_holder} and his balance is {acc5.balance} and his account type is {acc5.acc_type} and his reward points are {   acc5.reward_points}")


main()