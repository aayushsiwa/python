import random as r
user_name=str(input('Hello, what is your name:'))
choice=str(input('Would you like to play the game:'))
Result=''
comp_resp=r.randint(1,3)
if 'y' in choice:
    print('''Hello %s\nWelcome to the Stone Paper Scissor game \ncreated by Aayush Siwach
          \nThe rules for the game are:\n    %d.Stone > Scissor\n    %d.Stone > Paper\n    %d.Scissor > Paper
          \nYour options are:\n1=>Stone\n2=>Paper\n3=>Scissor'''%(user_name.capitalize(),1,2,3))
    while 'y' in choice:
        user_resp=int(input('Enter you option %s'%user_name.capitalize()))
        if user_resp==comp_resp:
            Result='No one wins'
        elif (user_resp==1 and comp_resp==2):
            Result= user_name+' wins\n'
        elif (user_resp==1 and comp_resp==3):
            Result= user_name+' wins\n'
        elif (user_resp==2 and comp_resp==1):
            Result='Computer wins\n'
        elif (user_resp==2 and comp_resp==3):
            Result='Computer wins\n'
        elif (user_resp==3 and comp_resp==1):
            Result='Computer wins\n'
        elif (user_resp==3 and comp_resp==2):
            Rsult=user_name+' wins\n'
        else:
            Result='Try Again\n'
        print(Result)
        choice=str(input('Would you like to play the game again:-'))
        if 'n' in choice:
            print('Ok %s ,thanks for visiting\nBut could you please provide your valuable feedback to improve our performance\n'%(user_name.capitalize()))
            def appenfile(fname):
                feed=input('==>')
                for i in range(1,1000):
                    f=open(fname,"a+")
                    data=str(i)+'. '+user_name.upper()+'->'+feed
                    f.write(data+'\n')
                    f.close()
                    break
            file='Feedback.txt'#this file will be created at the location where this program has been kept on your pc
            appenfile(file)
            print("Thanks for your feedback...we'll make necessary changes soon")
else:
    print('Ok %s ,thanks for visiting'%user_name.capitalize())
