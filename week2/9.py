""" Write a program asks for numeric user input. Instead the user types characters in the input box. 
The program normally would crash. But write try-except block so it can be handled properly. """

while True:
    try:    
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")