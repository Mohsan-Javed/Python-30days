email = input(f"Please enter your email: ")

index = email.index("@")
if index == -1:
    print(f"Your email is not valid.")
else:
    username = email[: index]
    domain = email[index + 1: ]
    print(f" ")
    print(f"Your username is {username} and your domain is {domain}.")
# index() finds the index of a given character