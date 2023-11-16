class Account:

    def __init__(self, owner: str, amount: int = 0):
        self.owner = owner
        self.amount = amount
        self._transactions: list[int] = []

    def handle_transaction(self, transaction_amount: int):
        if self.balance + transaction_amount < 0:
            raise ValueError("sorry cannot go in debt!")
        self._transactions.append(transaction_amount)
        return f"New balance: {self.balance}"

    def add_transaction(self, amount):
        if not isinstance(amount, int):
            raise ValueError("please use int for amount")
        else:
            return self.handle_transaction(amount)

    @property
    def balance(self):
        return self.amount + sum(self._transactions)

    def __str__(self):
        return f"Account of {self.owner} with starting amount: {self.amount}"

    def __repr__(self):
        return f"Account({self.owner}, {self.amount})"

    def __len__(self):
        return len(self._transactions)

    def __getitem__(self, idx: int):
        return self._transactions[idx]

    def __reversed__(self):
        return reversed(self._transactions)

    def __gt__(self, instance_account):
        return self.balance > instance_account.balance

    def __ge__(self, instance_account):
        return self.balance >= instance_account.balance

    def __eq__(self, instance_account):
        return self.balance == instance_account.balance

    def __add__(self, instance_account):
        new_account = Account(f"{self.owner}&{instance_account.owner}", self.amount + instance_account.amount)
        new_account._transactions = self._transactions + instance_account._transactions
        return new_account

