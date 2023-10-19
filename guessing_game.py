import random
import statistics


def start_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        # Generate the winning number
        winning_number = random.randint(1, 100)

        # Initialize variables to keep track of the player's attempts
        attempts = []

        while True:
            try:
                guess = int(input("Take a guess: "))
            except ValueError:
                print("Please enter a valid whole number.")
                continue

            attempts.append(guess)

            if guess < winning_number:
                print("Too low! Try a higher number.")
            elif guess > winning_number:
                print("Too high! Try a lower number.")
            else:
                print(f"Congratulations! You guessed the number in {len(attempts)} attempts.")
                break

        # Store the player's score
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing! Here's a summary of your game:")
            print(f"Number of guesses: {len(attempts)}")
            print(f"Mean of guesses: {statistics.mean(attempts)}")
            print(f"Median of guesses: {statistics.median(attempts)}")
            print(f"Mode of guesses: {statistics.mode(attempts)}")
            break


# Entry point of the game
start_game()
