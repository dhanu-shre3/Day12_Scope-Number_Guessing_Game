attempts = 10

computer_choice = 30
guess = int(input("Make a guess: "))

if guess > computer_choice:
    print("Too high, guess again")
    print(f"You have {attempts} attempts remaining to guess the number")

elif guess < computer_choice:
    print("Too Low, guess again")
    print(f"You have {attempts} attempts remaining to guess the number")
else:
    print(f"You got it! The number was {computer_choice}")

for attempt in range(1, attempts):
    attempts -= 1
    print(f"You have {attempts} attempts remaining to guess the number")
    