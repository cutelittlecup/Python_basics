class Piggy_bank:
    """Simple implementation of the functionality of the piggy_bank."""
    def __init__(self, balance: float, capacity: float) -> None:
        """
        Set capacity and start balance of the piggy_bank.

        :param balance: the amount of money in the piggy bank
        :param capacity: the largest amount of money that can be in the piggy bank
        """
        self.capacity = capacity
        self.balance = balance

    def check_balance(self) -> None:
        """Check how much money is in the piggy bank."""
        print(f"The current balance is {self.balance} coins")

    def add_money(self, get: float) -> None:
        """
        Add money to the piggy bank.

        :param get: set how much money need to add to the piggy bank
        :return: None
        """
        if (self.balance + get) > self.capacity:
            print(f"The size of the piggy bank is {self.capacity} coins. {self.capacity} coins have been added to the "
                  f"piggy bank.")
            self.balance = self.capacity
        else:
            self.balance = self.balance + get

    def take_money(self, take) -> None:
        """
        Take money from the piggy bank.

        :param take: set how much money need to take to the piggy bank
        :return:
        """
        if (self.balance - take) < 0:
            print(f"The balance of the piggy bank is {self.balance} coins. {self.balance} coins were taken from the "
                  f"piggy bank.")
            self.balance = 0
        else:
            self.balance = self.balance - take


Uno = Piggy_bank(0, 20.9)
Uno.add_money(15.5)
Uno.check_balance()
Uno.take_money(50)
