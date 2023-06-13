class User:
    """Simple class to model a user"""
    
    def __init__(self, name, age, gender):
        """Initialize a user object"""
        self.name = name
        self.age = age
        self.gender = gender
        
    def get_name(self):
        """Return user name"""
        return self.name
    
    def get_age(self):
        """Return user age"""
        return self.age
        
    def get_gender(self):
        """Return user gender"""
        return self.gender
    
    def __str__(self):
        return f"Name: {self.name.title()}\nAge: {self.age}\nGender: {self.gender.title()}"
    
        