import random as r
print("Hello this is a game based on your knowledge of 'Python'")
name=str(input('''By the way,
          What is your name?'''))
z=input('Do you want to play the game(Y/N):')
namec=name.capitalize()
if z=='y' or z=='Y':
    print('Good Luck !',namec)
elif z=='n' or z=='N':
    print('Ok',namec,'we hope you will try again later')
#now make a dictionary of questions and answers
questions=['who developed python','which type of software is python']
answers=['rossum','open source']
ques=r.choice(questions)
print(ques)
print('type the answer')
ans=input()
for j in range(0,12):
    for i in ans:
        if i == answers[j]:
            print('good')
            break
    
