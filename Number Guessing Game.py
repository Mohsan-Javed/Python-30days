import random

num = random.randint(1,100)

guess = 0
count = 0

print("Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 100.")


while guess != num:
    guess = int(input(f"Enter your guess: "))

    if guess < num:
        print("Too low! Guess again")
        count += 1
    elif guess > num:
            print("Too high! Guess again")
            count +=1
    else:
            print("Congratulations! You guessed it right!!")
            print(f"You guessed the number in {count} tries.")