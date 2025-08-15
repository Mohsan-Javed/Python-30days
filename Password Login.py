password = "Mohsan.64?"

print(f"Welcome!")
count = 0
guess = " "
print("Please enter your password to login: ")
while guess != password:
    guess = input(f" ")
    count += 1
    if count <= 3 and guess == password:
        print("Login Successful")
    elif guess != password and count != 3:
        print("Wrong password, Please try again: ")
    elif count == 3 and guess != password:
        print("You cannot access this account now!")
        break
    elif count < 3 and guess == password:
        print("Login Successful")