class Owner:
    def __init__(self, name, email, accountBalance):
        self.name = name
        self.email = email
        self.accountBalance = accountBalance

    def makePayment(self, amount):
        if amount <= self.accountBalance:
            self.accountBalance -= amount
            print(f"Payment of {amount} is made. Remaining balance is {self.accountBalance}")
        else:
            print("Not enough money!")

    