class BankAccount:
    def __init__(self, account_number, balance, type):
        self.__account_number = account_number  # double _ (__) makes it private
        self.__balance = balance
        self.type = type  # This one is PUBLIC because there is no __
        self._last_transaction = None  # This one is intended for internal use (single _)

    # Getter Methods
    def get_balance(self):
        return self.__balance

    def get_last_transaction(self):
        return self._last_transaction

    # Setter Methods
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self._last_transaction = f'Deposited {amount}'
            return True
        else:
            return False

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            self._last_transaction = f'Withdrew {amount}'
            return True
        else:
            return False


# Create a new bank account
my_account = BankAccount(12234456, 1000, "savings_account")

# Try and deposit money
if my_account.deposit(500):
    print(f'Successfully deposited! New balance is {my_account.get_balance()}')
    print(f'Last transaction: {my_account.get_last_transaction()}')

# Try to withdraw money
if my_account.withdraw(800):
    print(f'Successfully withdrew! New balance is {my_account.get_balance()}')
    print(f'Last transaction: {my_account.get_last_transaction()}')

# Try to change the _last_transaction
my_account._last_transaction = 'This should not be changed directly!'  # Not good practice!
print(f'Last transaction: {my_account.get_last_transaction()}')  # This will print the message you just set
