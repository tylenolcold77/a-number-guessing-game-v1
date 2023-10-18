# Import the random and statistics modules.

# Import necessary modules
import random
import statistics

# Create the start_game function.
# This function contains the main logic for the number guessing game.

# Define the start_game function
def start_game():
    # Display a welcome message to the player.
    print("Welcome to the guessing game.")

    # Ask the player to input a number between 1 and 100.
    input_number = int(input("Guess the number between 1 and 100:"))

    # Generate a random number between 1 and 100 as the solution.
    random_number = random.randint(1, 100)

    # Initialize the user's score.
    user_score = 0

    # Create a list to store the player's guesses.
    guess_list = []

    # Start a loop to allow the player to make guesses.
    while input_number != random_number:
        # Check if the input is outside the valid range (1-100).
        if input_number < 1 or input_number > 100:
            raise ValueError("Invalid number.")
        # Provide hints to the player based on their guess.
        if input_number > random_number:
            print("It's lower")
        else:
            print("It's higher")
        # Add the player's guess to the list.
        guess_list.append(input_number)
        # Ask the player to enter another number.
        input_number = int(input("Please enter a number:"))

    # When the correct guess is made, congratulate the player and increment their score.
    if input_number == random_number:
        user_score += 1
        print("Congratulations! You Win!!!")

    # Display game statistics to the player:
    # a. Number of attempts to guess the correct number.
    print(f"Attempts: {len(guess_list)}")
    # b. Mean (average) of the saved attempts.
    print(f"Mean: {statistics.mean(guess_list)}")
    # c. Median of the saved attempts.
    print(f"Median: {statistics.median(guess_list)}")
    # d. Mode of the saved attempts.
    print(f"Mode: {statistics.mode(guess_list)}")

# Check if this script is the main entry point of the program.
if __name__ == '__main__':
    try:
        # Call the start_game function to begin the game.
        start_game()

        # Ask the player if they want to play again.
        reply = input("Start again: Y or N")
        while reply.upper() == 'Y':
            start_game()
            reply = input("Start again: Y or N")

        # Display a goodbye message when the player decides to quit.
        print("Goodbye! Thanks for playing.")

    except ValueError:
        print("Invalid range. Your input must be between 1 and 100")
