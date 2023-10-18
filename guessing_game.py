"""
Data Analysis Techdegree
Project 1 - A Number Guessing Game
--------------------------------
"""

# Import the random and statistics modules.

# Create the start_game function.
# Write your code inside this function.

#   When the program starts, we want to:
#   ------------------------------------
#   1. Display an intro/welcome message to the player.
#   2. Store a random number as the answer/solution.
#   3. Continuously prompt the player for a guess.
#     a. If the guess is greater than the solution, display to the player "It's lower".
#     b. If the guess is less than the solution, display to the player "It's higher".

#   4. Once the guess is correct, stop looping, inform the user they "Got it" and store the number of guesses it took in a list.
#   5. Display the following data to the player
#     a. How many attempts it took them to get the correct number in this game
#     b. The mean of the saved attempts list
#     c. The median of the saved attempts list
#     d. The mode of the saved attempts list
#   6. Prompt the player to play again
#     a. If they decide to play again, start the game loop over.
#     b. If they decide to quit, show them a goodbye message.

# ( You can add more features/enhancements if you'd like to. )
import random
import statistics

# Kick off the program by calling the start_game function.
guess_list = []
def start_game():
    print("Welcome to the guessing game.")
    input_number = int(input("the number between 0 and 100:"))

    random_number = random.randint(1,100)
    user_score = 0
    while input_number != random_number:
        if input_number < 0 or input_number > 100:
            raise ValueError("Invalid number.")
        if input_number > random_number:
            print("Too big")
        else:
            print("Too small")
        guess_list.append(input_number)
        input_number = int(input("Please enter a number:"))
    if input_number == random_number:
        user_score += 1
        print("Congratulation! You Win!!!")



if __name__=='__main__':
    try:
        start_game()
        reply = input("Start again: Y or N")
        while reply.upper() == 'Y':
            start_game()
            reply = input("Start again: Y or N")
        print("ByeBye! Thanks for playing.")
    except ValueError:
        print("Invalid range. Your input must between 1 and 100")
