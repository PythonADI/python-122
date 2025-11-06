"""
Create class with following attributes
- username should be only lowercase
- email should contain @ and should end with .com
- first name and last name, make sure that these fields are only strings!
- phone number that should start with +995 and should have length of 12
"""

# PascalCase
class User:
    def __init__(self, username, email, first_name, last_name, phone_number):
        if not username.islower():
            raise ValueError("username must be in lowercase")
        self.username = username

        if "@" not in email or not email.endswith(".com"):
            raise ValueError("email not correct")
            
        self.email = email

        if not first_name.isalpha() or not last_name.isalpha():
            raise ValueError("first name or last name is not correct")
            
        self.first_name = first_name
        self.last_name = last_name

        if not phone_number.startswith("+995") or len(phone_number) != 13:
            raise ValueError("phone number is not correct")

        self.phone_number = phone_number

    
    def __str__(self):
        return f"{self.username} | {self.email} | {self.first_name} {self.last_name} | {self.phone_number}"


u = User(
    "gw", 
    "GeorgeWashington@gmail.com", 
    "George", 
    "Washington", 
    "+995 997 77 88 99".replace(" ", "")
)

print(u)