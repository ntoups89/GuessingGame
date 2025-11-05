# Nathaniel Toups #
# CIS 261 #
# Guessing Game #

import random
def number_guessing_game():
    secert_number = random.randint(1, 10)
    attempts = 0

    print("Welcome to the number guessing game!")
    while True:
        number_guessing_game()
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

    print("I have selected a number between 1 and 10. Try to guess it.")

    while True:
        try:
            guess_input = input("Enter your guess (1-10): ")
            guess = int(guess_input)
            attempts += 1
        except ValueError:
            print("Invaild input. Please enter a whole number.")
            continue
        if guess < 1 or guess > 10:
            print("Your guess must be between 1 and 10.")
            continue
        if guess < secert_number:
            print("Too low! Try again.")
        elif guess > secert_number:
            print("Too High! Try again.")
        else:
            print(f"Congratulations! You guessed the number {secert_number} correctly.")
            print(f"It took you {attempts} attempts.")
            break
if __name__ == "__main__":
    number_guessing_game()

