#import random module 
import random as r
''' Print multiline instruction 
 performstring concatenation of string '''
user_name=str(input("Please enter your name:"))
print("Winning Rules of the Rock paper scissor game as follows: \n"
                                +"Rock vs paper->paper wins \n"
                                + "Rock vs scissor->Rock wins \n"
                                +"paper vs scissor->scissor wins \n") 
while True: 
    print("Enter choice \n 1=Rock \n 2=paper \n 3=scissor \n")    
    # take the input from user 
    choice = int(input("Your turn: "))
    # looping until user enter invalid input 
    while choice > 3 or choice < 1: 
        choice =int(input("enter valid input: "))
    # initialize value of choice_name variable 
    # corresponding to the choice value 
    if choice == 1: 
        choice_name = 'Rock'
    elif choice == 2: 
        choice_name = 'paper'
    else: 
        choice_name = 'scissor'
    # print user choice  
    print("Your choice is: " + choice_name) 
    print("\nNow its computer turn.......") 
    # Computer chooses randomly any number  
    # among 1 , 2 and 3. Using randint method 
    # of random module 
    comp_choice = r.randint(1, 3) 
    # looping until comp_choice value  
    # is equal to the choice value 
    while comp_choice == choice: 
        comp_choice = r.randint(1, 3) 
    # initialize value of comp_choice_name  
    # variable corresponding to the choice value 
    if comp_choice == 1: 
        comp_choice_name = 'Rock'
    elif comp_choice == 2: 
        comp_choice_name = 'paper'
    else: 
        comp_choice_name = 'scissor'
    print("Computer choice is: " + comp_choice_name) 
    print(choice_name + " V/s " + comp_choice_name) 
    # condition for winning 
    if((choice == 1 and comp_choice == 2) or
      (choice == 2 and comp_choice ==1 )): 
        print("Paper wins,", end = "") 
        result = "Paper"
    elif((choice == 1 and comp_choice == 3) or
        (choice == 3 and comp_choice == 1)): 
        print("Rock wins,", end = "") 
        result = "Rock"
    else: 
        print("Scissor wins,", end = "") 
        result = "Scissor"
    # Printing either user or computer wins
    if result == choice_name: 
        print(" Congratulations, you win") 
    else: 
        print(" Computer wins, better luck next time") 
    print("Do you want to play again? (Y/N)") 
    ans = input()
    if ans == 'y' or ans == 'Y': 
        print()
    elif ans=='n' or ans=='N':
        break
    # if user input n or N then condition is True
    # after coming out of the while loop
    # we print thanks for playing
changeslst=[]
print("\nThanks for playing",user_name) 
feedback=int(input("Please tell us how was the game\n|1-Awful| |2-Bad| |3-Satisfactory| |4-Good| |5-Outstanding|\n->"))
if feedback==1 or feedback==2 or feedback==3 or feedback==4:
    changes=input("Enter the changes you want to be made to the game->")
    changeslst.append(changes)
    print("Thanks for your feedback...we'll make necessary changes soon")
