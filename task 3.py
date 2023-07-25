class Piggy_bank:
    def __init__(self, balance, capacity):
        self.capacity = capacity
        self.balance = balance

    def balance(self):
        print('Текущий баланс ' + str(self.balance) + ' монет')

    def getmoney(self, get):
        if (self.balance + get) > self.capacity:
            print('Невозможно добавить такую сумму')
        else:
            self.balance = self.balance + get


Uno = Piggy_bank(0, 20)
Uno.getmoney(5)
Uno.balance()