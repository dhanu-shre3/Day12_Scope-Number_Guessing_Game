import random 

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#function to set difficulty
level = input("Choose a difficulty. Type 'easy' or 'hard': ")

# def set_difficulty():

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 nad 100.")



computer_choice = random.randint(1, 100)
guess_again = True

#attempts
if level == "easy":
    turns = 10
else:
    turns = 5

while guess_again:
    for turns in range(-10):


        guess = int(input("Make a guess: "))





        if guess > computer_choice:
            print("Too high, guess again")
            turns += 1
            print(f"You have {turns} attempts remaining to guess the number")

            
        elif guess < computer_choice:
            print("Too Low, guess again")
            turns += 1
            print(f"You have {turns} attempts remaining to guess the number")
        elif turns == 0:
            guess_again = False

        else:
            print(f"You got it! The number was {computer_choice}")
            guess_again = False


 

    