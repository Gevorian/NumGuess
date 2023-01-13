import random

# Generate a random number between 1 and 100
target = random.randint(1, 100)

# Initialize the number of guesses to 0
guesses = 0

# Start the game loop
while True:
    # Get the user's guess
    guess = int(input("Guess a number between 1 and 100: "))
    guesses += 1

    # Check if the guess is too high, too low, or correct
    if guess > target:
        print("Too high! Try again.")
    elif guess < target:
        print("Too low! Try again.")
    else:
        print(f"Congratulations! You guessed the number in {guesses} guesses.")
        break
