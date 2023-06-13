from User import User
from BankAccount import BankAccount
from Menu import menu


bank_accounts = []
class MenuChoices():
    """Class to create accounts and user info"""
    
    
    @staticmethod
    def create_account():
        """Creates new account"""
        name = input("Enter client name: ")
        age = int(input("Enter client age: "))
        gender = input("Enter client gender: ")
        
        user = User(name, age, gender)
        
        acc_number = int(input("Enter account number: "))
        acc_type = input("Enter client account type: ")
        balance = float(input("Enter initial deposit amount: "))
        
        bank_account = BankAccount(user, acc_number, acc_type, balance)
        
        print("Account created successfully!")
        bank_accounts.append(bank_account)
    
    @staticmethod
    def show_account_details():
        """Displays account details"""
        account = int(input("Enter account number: "))
        for bank_account in bank_accounts:
            if bank_account.get_acc_number() == account:
                 menu.show_accounts_menu()
                 print(bank_account)
                 return
            else:
                print("Account not found!")
        
    @staticmethod   
    def get_deposit_info():
        """Conducts deposit methods"""
        account = int(input("Enter account number: "))
        for bank_account in bank_accounts:
            if bank_account.get_acc_number() == account:
                menu.show_deposit()
                amount = float(input())
                bank_account.deposit(amount)
                return
            else:
                print("Account not found")
    
    @staticmethod
    def get_withdrawal_info():
        """Conducts withdrawal methods"""
        account = int(input("Enter account number: "))
        for bank_account in bank_accounts:
            if bank_account.get_acc_number() == account:
                menu.show_withdrawal()
                amount = float(input())
                bank_account.withdrawal(amount)
                return
            else:
                print("Account not found!")
        
    @staticmethod    
    def choices(choice):
        """Returns menu choices"""
        if choice == 1:
            MenuChoices.create_account()
        elif choice == 2:
            MenuChoices.show_account_details()
        elif choice == 3:
            MenuChoices.get_deposit_info()
        elif choice == 4:
            MenuChoices.get_withdrawal_info()
        elif choice == 5:
            exit()
        else:
            print("Invalid Choice!")
            
            
if __name__ == "__main__":
    while True:
        menu.show_menu()
        choice = int(input("Enter your choice: "))
        MenuChoices.choices(choice)
        if choice == 5:
            print("Thank you for using banking system!")
            break

            
        
    
        
        
        
        
    
