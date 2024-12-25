import random
# library that we use in order to choose 
# on random words from a list of words
print('Hello this a game based on computer')
name = input("By the way what is your name? ")
# Here the user is asked to enter the name first
z=input('Do you want to play the game(Y/N):')
while z=='y'or z=='Y':
    print("Good Luck ! ", name)
    break
words = ['computer','programming','python','list','tuples','html','monitor','idle']
    # Function will choose one random
    # word from this list of words
word = random.choice(words)
print("Guess the characters") 
guesses = ''
    # any number of turns can be used here
turns = len(word)+len(name)-4
while turns > 0:
    failed = 0
         # counts the number of times a user fails
    # all characters from the input
    # word taking one at a time.
for char in word:
    if char in guesses:
        print(char)
    else:
        print("_")
        # comparing that character with
        # the character in guesses          
            # for every failure 1 will be
            # incremented in failure
failed += 1
if failed == 0:
    print("You Win")
    print("The word is: ", word)
        # user will win the game if failure is 0
        # and 'You Win' will be given as output
        # this print the correct word
    # if user has input the wrong alphabet then
    # it will ask user to enter another alphabet
guess = input("guess a character:")
    # every input character will be stored in guesses 
guesses += guess 
    # check input with the character in word
if guess not in word:
    turns -= 1
    print("Wrong")
        # if the character doesn’t match the word
        # then “Wrong” will be given as output 
        # this will print the number of
        # turns left for the user
    print("You have", + turns, 'more guesses')         
if turns == 0:
    print("You Loose")
