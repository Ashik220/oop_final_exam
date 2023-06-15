from transaction import*
class Account:
    def __init__(self, account_id_number):
        self.account_id_number = account_id_number
        self.balance = 0
        self.total_deposit = []
        self.total_withdraw = []
        self.transactions = []
        self.loans = []
        self.total_bank_equity = 10000


    def deposit(self, amount):
        self.balance += amount
        self.total_deposit.append(amount)
        transaction = vars(Transaction('Deposit',amount))
        self.transactions.append(transaction)
        return self.balance

    def withdraw(self, amount):
        if amount < 0:
            print('Invalid entry')
            return None
        if amount > self.balance:
            print('Withdrawal excees current balance')
        if self.balance >= amount:
            self.balance -= amount
            self.total_withdraw.append(amount)
            transaction = vars(Transaction('Withdraw',amount))
            self.transactions.append(transaction)
        else:
            print('Not enough balance')
        return self.balance
    
    def take_loan(self):
        amount = input('enter loan amount:')
        amount = int(amount)      
        if amount <= self.balance * 2:
            self.balance -= amount
            self.loans.append(amount)
        else:
            print()
        return amount

    # def balance_transfer(self,account_id_number):
    #     self.account_id_number = account_id_number
    #     account = Account(account_id_number)
    #     amount = input('Enter amount to transer:')
    #     amount = int(amount)
    #     account = account.withdraw(amount)
    #     tr = input('Enter account_id_number to transfer balance:')
    #     account = Account(tr)
    #     account = account.deposit(amount)
    #     self.transactions.append(Transaction(amount,'Balance Transfer'))

    def check_transaction(self):
        if self.balance == 0:
            print('No transaction record')
        else:
            for transaction in self.transactions:
                print(transaction)
        return ''

    def total_balance(self):
        total_deposit_sum = 0
        total_withdraw_sum = 0
        
        for balance in self.total_deposit:
            total_deposit_sum += balance
        for i in self.total_withdraw:
            total_withdraw_sum += i
        total_sum = total_deposit_sum - total_withdraw_sum
        return total_sum
    
    def total_loan(self):
        total_loan = 0
        for loan in self.loans:
            total_loan += loan
        return total_loan

    def exit_loan(self):
        total_loan = self.total_loan()
        if total_loan > self.total_bank_equity:
            print('Equity in critcal stage, Please stop the loan feature')
        return ''