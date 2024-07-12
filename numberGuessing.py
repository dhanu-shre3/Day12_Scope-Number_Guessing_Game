import random 

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 nad 100.")
level = input("Choose a difficulty. Type 'easy' or 'hard': ")

if level == "easy":
    print("You have 10 attempts remaining to guess the number")
else:
    attempts = 5
    print("You have 5 attempts remaining to guess the number")


computer_choice = random.randint(1, 100)
guess_again = True

#attempts


while guess_again:
    guess = int(input("Make a guess: "))

    if level == 'easy':
        attempts = 10
        for attempt in range(1, attempts):
            attempts -= 1
        if guess > computer_choice:
            print("Too high, guess again")
            print(f"You have {attempts} attempts remaining to guess the number")

        elif guess < computer_choice:
            print("Too Low, guess again")
            print(f"You have {attempts} attempts remaining to guess the number")
        else:
            print(f"You got it! The number was {computer_choice}")
            guess_again = False

  

    