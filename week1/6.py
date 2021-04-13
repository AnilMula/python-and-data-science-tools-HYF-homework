""" Guess a number game - between 1 to 9. 
Note : User is prompted to enter a guess. 
If the user guesses wrong then the prompt appears again until the guess is correct, 
on successful guess, user will get a "Well guessed!" message, and the program will exit. """
import random

random_number = random.randint(1, 10)            ## module randint is to generate numbers between the range
while True:
    user_guess = int(input("Guess a number"))
    if random_number == user_guess:
        print("Well guessed!")
        break                                    ## to exit a loop