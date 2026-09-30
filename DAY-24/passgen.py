import random
name = input("Enter your name: ").title()
dob = input("Enter your date of birth (dd-mm-yyyy): ")
spc = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+']

password = name + random.choice(spc) 
print(f"Your generated password is: {password}")  

