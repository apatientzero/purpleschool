class BankAccount:
    _accounts_created = 0

    def __init__(self, owner: str, account_number: str | int, balance: float = 0.0):
        """Init bank account"""
        if balance < 0:
            raise ValueError('The balance cannot be negative')

        self.owner = owner
        self.account_number = account_number
        self._balance = float(balance)  # ← используем _balance сразу

        BankAccount._accounts_created += 1

    @property
    def balance(self) -> float:
        """Balance (only read)"""
        return self._balance

    def deposit(self, amount: float) -> None:
        """Adding $ to account"""
        if amount <= 0:
            raise ValueError('The deposit amount must be positive')
        self._balance += amount

    def withdraw(self, amount: float) -> None:
        """Withdrawing money"""
        if amount <= 0:
            raise ValueError('The withdrawal amount must be positive')
        if amount > self._balance:
            raise ValueError('Insufficient funds in the account')
        self._balance -= amount

    def transferto(self, otheraccount: 'BankAccount', amount: float) -> None:
        """Transfer money to another account"""
        if not isinstance(otheraccount, BankAccount):
            raise TypeError('The target account must be an instance of BankAccount')
        if amount <= 0:
            raise ValueError('The transfer amount must be positive')
        if amount > self._balance:
            raise ValueError('Insufficient funds in the account for the transfer')
        self._balance -= amount
        otheraccount._balance += amount

    def info(self) -> str:
        """Short information"""
        return f'Account {self.account_number} owner {self.owner}. Balance: {self._balance:.2f}'

    @classmethod
    def getaccountscreated(cls) -> int:
        """Returns the number of created accounts"""
        return cls._accounts_created

# If __name == '__main__'
if __name__ == '__main__':
    # Create account
    account1 = BankAccount("Mike Tyson", "321654", 1000)
    account2 = BankAccount("Halle Berry", "67890")

    print(account1.info())
    print(account2.info())

    # Operation
    account1.deposit(500)
    account1.withdraw(200)
    account1.transferto(account2, 300)

    print(account1.info())
    print(account2.info())
    print(BankAccount.getaccountscreated())
