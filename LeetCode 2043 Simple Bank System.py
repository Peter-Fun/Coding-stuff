class Bank(object):

    def __init__(self, balance):
        """
        :type balance: List[int]
        """
        self.bal = balance

    def transfer(self, account1, account2, money):
        """
        :type account1: int
        :type account2: int
        :type money: int
        :rtype: bool
        """
        if account1 > len(self.bal) or account1 < 1 or account2 > len(self.bal) or account2 < 1 or self.bal[account1-1] < money:
            return False
        self.bal[account1-1] -= money
        self.bal[account2-1] += money
        return True

    def deposit(self, account, money):
        """
        :type account: int
        :type money: int
        :rtype: bool
        """
        if account > len(self.bal) or account < 1:
            return False
        self.bal[account-1] += money
        return True
        

    def withdraw(self, account, money):
        """
        :type account: int
        :type money: int
        :rtype: bool
        """
        if account > len(self.bal) or account < 1 or self.bal[account-1] < money:
            return False
        self.bal[account-1] -= money
        return True


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
