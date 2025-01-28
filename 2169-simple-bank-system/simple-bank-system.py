class Bank:
    def __init__(self, balance: List[int]):
        self.balance = balance
        self.n = len(balance)
        print(balance)
    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if 0 <= account1 - 1< self.n and 0 <= account2 - 1 < self.n:
            if self.balance[account1 - 1] >= money:
                self.balance[account1 - 1] -= money
                self.balance[account2 - 1] += money
            else:
                return False
        else:
            return False
        return True

    def deposit(self, account: int, money: int) -> bool:
        if 0 <= account - 1 < self.n:
            self.balance[account - 1] += money
        else:
            return False
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if 0 <= account -1 < self.n:
            if money <= self.balance[account - 1]:
                self.balance[account - 1] -= money
            else:
                return False
        else:
            return False
        return True


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)