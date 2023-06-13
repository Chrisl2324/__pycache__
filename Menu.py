class menu:
    """Class to represent menu choices"""
    
    @staticmethod
    def show_menu():
        """Displays bank menu"""
        print("Welcome to banking system!")
        print("==========================")
        print("1. Create Account")
        print("2. View Account Details")
        print("3. Deposit to Account")
        print("4. Withdraw from Account")
        print("5. Exit")
        print("==========================")
        
    @staticmethod
    def show_deposit():
        """Shows deposit menu"""
        print("---------------Deposit------------")
        print("==================================")
        print("How much would you like to deposit?")
        
    @staticmethod
    def show_withdrawal():
        """Shows withdrawal menu"""
        print("-------------Withdrawal-------------")
        print("====================================")
        print("How much would you like to withdraw?")
        
    @staticmethod
    def show_accounts_menu():
        """Heading for displaying accounts"""
        print("-----------Account Details------------")
        print("======================================")
        