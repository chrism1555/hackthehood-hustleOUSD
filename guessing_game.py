# Guessing Game - Christian, KJ, Deney, Alicia, Candy, Josue

import random

def generate_random_number():
    return random.randint(1, 100)

random_number = generate_random_number()
print(f"Your random number is: {random_number}")

def get_user_guess():
    while True:
        try:
            # HOw do i check that the user input matches the rando, number generated?
            # Hint: use if /else statement
            user_input = int(input("Enter new guess "))
        except:
            print("Try again")


get_user_guess()



def play_guessing_game():
    guessing_game = play_guessing_game()