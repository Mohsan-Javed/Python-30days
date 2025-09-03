import random

choices = ["Snake", "Water", "Gun"]

user_choice = ""
comp_choice = ""
player_score = 0
computer_score = 0
draws = 0

while True:
    comp_choice = random.choice(choices)

    user_choice = input("Enter your choice (Snake/Water/Gun) or 'quit' to exit: ")

    user_choice = user_choice.lower()
    user_choice = user_choice.capitalize()

    if user_choice == "Quit":
        print("Thank you for playing this game!")
        if player_score and computer_score and draws != 0:
            print(f"The scores are: Your Score = {player_score} | Computer Score = {computer_score} | Draws = {draws}")
        break

    if user_choice not in choices:
        print(f"Invalid choice, Please try again!")
        continue

    print(f"Your Choice: {user_choice}")
    print(f"Computer's Choice: {comp_choice}")

    result = ""

    if user_choice == comp_choice:
        result = "A Draw"
        draws = draws + 1

    elif (user_choice == "Snake" and comp_choice == "Water"
      or user_choice == "Water" and comp_choice == "Gun"
      or user_choice == "Gun" and comp_choice == "Snake"):
        result ="You win"
        player_score = player_score + 1

    else:
        result = "Computer wins"
        computer_score = computer_score + 1

    print(f"Result is: {result}")

    answer = input("Do you want to play again(Yes or No)? ")
    answer.lower()
    answer.capitalize()

    if answer == "No":
        print("Thank you for playing!")
        print(f"The scores are: Your Score = {player_score} | Computer Score = {computer_score} | Draws = {draws}")
        break
    else:
        continue