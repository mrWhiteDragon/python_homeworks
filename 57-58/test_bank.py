import unittest

class BankAccount:
    def __init__(self, account_holder, initial_balance = 0):
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        if amount <= 0:
            return 'Сумма вклада должна быть положительной'
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= 0:
            return 'Сумма снятия должна быть положительной'
        if amount > self.balance:
            return 'Недостаточно средств на счете'
        self.balance -= amount
        return self.balance

    def get_balance(self):
        return self.balance

bank_account_1 = BankAccount('Сергей')
print(bank_account_1.balance)
print(bank_account_1.deposit(-500000))
print(bank_account_1.deposit(500000))
print(bank_account_1.withdraw(-600000))
print(bank_account_1.withdraw(600000))
print(bank_account_1.withdraw(300000))
print(bank_account_1.get_balance())


class TestBankAccount(unittest.TestCase):
    def test_init_balance(self):
        bank_account = BankAccount('Cергей')
        self.assertEqual(bank_account.balance, 0)

    def test_deposit(self):
        bank_account = BankAccount('Cергей')
        self.assertEqual(bank_account.deposit(1000000), 1000000)

    def test_not_positive_deposit(self):
        bank_account = BankAccount('Cергей')
        self.assertEqual(bank_account.deposit(-1000000), 'Сумма вклада должна быть положительной')

    def test_withdraw(self):
        bank_account = BankAccount('Cергей')
        bank_account.deposit(1000000)
        self.assertEqual(bank_account.withdraw(200000), 800000)

    def test_not_positive_withdraw(self):
        bank_account = BankAccount('Cергей')
        bank_account.deposit(1000000)
        self.assertEqual(bank_account.withdraw(-200000), 'Сумма снятия должна быть положительной')

    def test_excceeding_withdraw(self):
        bank_account = BankAccount('Cергей')
        bank_account.deposit(1000000)
        self.assertEqual(bank_account.withdraw(1200000), 'Недостаточно средств на счете')

    def test_get_balance(self):
        bank_account = BankAccount('Cергей')
        self.assertEqual(bank_account.get_balance(), 0)

if __name__ == "__main__":
    unittest.main()




