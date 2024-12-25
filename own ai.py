import pyttsx3
from playsound import playsound
converter=pyttsx3.init()
converter.setProperty('rate',150)
converter.setProperty('volume',10)
converter.say('What is your name user?')
print('What is your name user?')
name=str(input())
converter.say('Hello %s I am your assistant Preeti....What can i do for you sir?'%name)
print('Hello %s I am your assistant Preeti....What can i do for you sir?'%name)
task=str(input())
while 'music' in task:
    converter.say('Which one sir?')
    print('Which one sir?')
    music=str(input())
    if 'army' in music:
        playsound('Youre In The Army Now.mp3')
        break
    elif 'brother' in music:
        playsound('Brothers In Arms.mp3')
        break
    else:
        converter.say('Sorry sir please try again')
        music=str(input())
while 'nothing' in task:
    converter.say('Ok bye %d'%name)
    print('Ok bye %d'%name)
    break
