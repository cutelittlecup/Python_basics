class Piggy_bank:
    def __init__(self, balance, capacity):
        self.capacity = capacity
        self.balance = balance

    def check_balance(self):
        print(f"The current balance is {self.balance} coins")

    def get_money(self, get):
        if (self.balance + get) > self.capacity:
            print(f"The size of the piggy bank is {self.capacity} coins. {self.capacity} coins have been added to the "
                  f"piggy bank.")
            self.balance = self.capacity
        else:
            self.balance = self.balance + get

    def take_money(self, take):
        if (self.balance - take) < 0:
            print(f"The balance of the piggy bank is {self.balance} coins. {self.balance} coins were taken from the "
                  f"piggy bank.")
            self.balance = 0
        else:
            self.balance = self.balance - take


Uno = Piggy_bank(0, 20)
Uno.get_money(21)
Uno.check_balance()
Uno.take_money(50)
