# return your age

birth_year = input("What year were you born \n")

age = 2020 - int(birth_year)

print(f"Your age is {age}")

# password checker

username = input("Enter your username \n")
password_one = input("Enter your password \n")

number = len(password_one)
hashed = "*"*number
print(f"Hey {username} your password {hashed} is {number} letters long")