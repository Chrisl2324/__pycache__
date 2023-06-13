from User import User

class BankAccount(User):
    """Class to created bank account for user"""
    
    def __init__(self, user, acc_number, acc_type, balance=0):
        """Initialize bank account"""
        super().__init__(user.name, user.age, user.gender)
        self.acc_number = acc_number
        self.acc_type = acc_type
        self.balance = balance
        
    def get_acc_number(self):
        """Return account number"""
        return self.acc_number
    
    def get_acc_type(self):
        """Return account type"""
        return self.acc_type
    
    def get_balance(self):
        """Return balance"""
        return self.balance
    
    def __str__(self):
        """Return string format of user and bank account info"""
        user_info = super().__str__()
        bank_info = f"Account Number: {self.acc_number}\nAccount Type: {self.acc_type}\nBalance: ${self.balance:.2f}"
        return f"{user_info}\n{bank_info}"
    
    def deposit(self, amount):
        """Deposit to bank acccount"""
        self.balance += amount
        return self.balance
    
    def withdrawal(self, amount):
        """Withdraw from bank account"""
        if amount > self.balance:
            print("Amount exceeds balance!")
        else:
            self.balance -= amount
        return self.balance

