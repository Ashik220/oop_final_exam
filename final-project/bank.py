from user import*
class Bank:
    def __init__(self):
        self.user_list = {}
        self.account_id_number = 0

    def create_account(self):
        user_name = input("Enter your name:")
        user_name = user_name
        user_password = input("Enter your password:")
        user_password = user_password
        new_account = User(user_name,user_password)
        new_account = vars(new_account)
        self.user_list[self.account_id_number] = []
        self.user_list[self.account_id_number].append(new_account)
        self.account_id_number += 1