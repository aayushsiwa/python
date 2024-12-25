import random as r
import datetime as d
current_time=d.datetime.now()
lst=[]
res=[]
user_name=str(input('Hello, what is your name:'))
choice=str(input('Would you like to play the game:'))
Result=''
comp_resp=r.randint(1,3)
def appendfile(fname):
                f=open(fname,"a+")
                if 'n' in choice or 'N' in choice:
                    log_data=('<TR>'+'\n'+'<TH>NAME</TH>'+'\n'+'<TH>TIME</TH>'+'\n'+
                    '\n'+'</TR>'+'<TR>'+'\n'+'<TD>'+user_name.upper()+
                    '\n'+'<TD>'+str(current_time)+'\n'+'</TR>'+'</TABLE>')
                else:
                    log_data=('<TR>'+'\n'+'<TH>NAME</TH>'+'\n'+'<TH>TIME</TH>'+'\n'+
                    '<TH>No. OF TIMES GAME PLAYED</TH>'+'\n'+'<TH>No. OF TIMES GAME WON</TH>'+
                    '\n'+'<TH>No. OF TIMES GAME LOST</TH>'+'\n'+'<TH>No. OF TIES</TH>'+'\n'+
                    '<TH>FEEDBACK</TH>'+'\n'+'</TR>'+'<TR>'+'\n'+'<TD>'+user_name.upper()+
                    '\n'+'<TD>'+str(current_time))
                f.write('<BODY BACKGROUND="a.png">'+'<table border="10" border color="Black" bgcolor="Orange" cellpadding="10" cellspacing="5">'+log_data+'\n')
                f.close()
filename='STP log.html'
appendfile(filename)
if 'y' in choice or 'Y'  in choice:
    print('''Hello %s\nWelcome to the Stone Paper Scissor game \ncreated by Aayush Siwach
          \nThe rules for the game are:\n    %d.Stone > Scissor\n    %d.Stone > Paper\n    %d.Scissor > Paper
          \nYour options are:\n1=>Stone\n2=>Paper\n3=>Scissor'''%(user_name.capitalize(),1,2,3))
    while 'y' in choice or 'Y' in choice:
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
        lst.append(choice)
        if Result==user_name+' wins\n':
            res.append(1)
        elif Result=='Computer wins\n':
            res.append(2)
        else:
            res.append(3)
        user_win=res.count(1)
        comp_win=res.count(2)
        tie=res.count(3)
        if 'n' in choice or 'N' in choice:
            print('Ok %s ,thanks for playing the game\nBut could you please provide your valuable feedback to improve our performance\n'%(user_name.capitalize()))
            def appenfile(fname):
                feed=input('==>')
                f=open(fname,"a+")
                data='<TD>'+str(len(lst))+'\n'+'<TD>'+str(user_win)+'\n'+'<TD>'+str(comp_win)+'\n'+'<TD>'+str(tie)+'\n'+'<TD>'+feed+'</TR>'
                f.write(data+'\n'+'</table>'+'<br>')
                f.close()
            file='STP log.html'#this file will be created at the location where this program has been kept on your pc
            appenfile(file)
            print("Thanks for your feedback...we'll make necessary changes soon")
else:
    print('Ok %s ,thanks for visiting.'%user_name.capitalize())
