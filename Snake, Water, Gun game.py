import random

choices = ["Snake", "Water", "Gun"]
comp_choice = random.choice(choices)

user_choice = input("Enter your choice (Snake/Water/Gun) or 'quit' to exit: ")

user_choice = user_choice.lower()
user_choice = user_choice.capitalize()

print(f"Your Choice: {user_choice}")
print(f"Computer's Choice: {comp_choice}")

player_score = 0
computer_score = 0
draws = 0
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
print(f"The scores are: Your Score = {player_score} | Computer Score = {computer_score} | Draws = {draws}")