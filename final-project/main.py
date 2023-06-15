from bank import*
from account import*
from transaction import*
def main():
    bank = Bank()
    account = Account(0)
    # # user1 = bank.create_account()
    

    # # print(bank.user_list)

    
    # user1 = account.deposit(100)
    # user1 = account.deposit(200)
    # user1 = account.withdraw(150)
    # print(user1)

    # user2 = account.deposit(300)
    # user2 = account.withdraw(50)
    
    
    # # user2 = account.deposit(200)
    # # print(user2)
    # # user1 = account.withdraw(50)
    # user1 = account.check_transaction()
    # print(user1)
    
    # # user2 = account.withdraw(20)
    
    # user1 = account.take_loan()
    # user2 = account.total_loan()
    
    # print(account.total_balance())
    # print(account.total_loan())
    # print(account.exit_loan())

    while True:
        print('press c to create account')
        print('press d to deposit')
        print('press w to withdraw')
        print('press l to take loan')
        print('press t to check transaction')
        print('press b to check total balance')
        print('press a to check total loan')
        print('press e to exit loan')
        print()
        take_input = input('Inster the key to query:')
        if take_input == 'c':
            create_acc = bank.create_account()
            print('account created successfully')
        
        elif take_input == 'd':
            amount = input('enter amount to deposit:')
            amount = int(amount)
            depo = account.deposit(amount)
            print(f'deposite successfull, current amount {depo}')
            print()
        
        elif take_input == 'w':
            amount = input('enter amount to withdraw:')
            amount = int(amount)
            withd = account.withdraw(amount)
            print(f'current amount {withd}')
            print()

        elif take_input == 'l':
            loan = account.take_loan()
            print(f'you have got {loan} as loan')
            print()
        
        elif take_input == 't':
            trans = account.check_transaction()
            print(trans)
            print()
        
        elif take_input == 'b':
            balance = account.total_balance()
            print(f'your available balance is {balance}')
            print()
        
        elif take_input == 'a':
            total_loan_amount = account.total_loan()
            print(f'total loan amount is {total_loan_amount}')
            print()
        
        elif take_input == 'a':
            exit_l = account.exit_loan()
            print()
if __name__ == '__main__':
    main()