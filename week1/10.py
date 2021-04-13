""" Accept a string from user and remove the characters which have odd index values of a given string and print them. """

user_input = input("enter a string \n")
i = len(user_input)                 ## get the length of string
j = 1                               ## make it 0 for even index characters
while i > 0 :
    print(user_input[j])
    j = j + 2
    i = i -2