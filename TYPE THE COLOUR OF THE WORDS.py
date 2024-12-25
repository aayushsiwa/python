import tkinter 
import random 
colours = ['Red','Blue','Green','Pink','Black', 
           'Yellow','Orange','White','Purple','Brown'] #you can add any color here just the way others have been....
score = 0
timeleft =60#you can change the time from here
def startGame(event): 
    if timeleft == 60:#make sure you do the time changes here also 
        countdown() 
    nextColour() 
def nextColour(): 
    global score 
    global timeleft 
    if timeleft > 0: 
        e.focus_set()
        if e.get().lower() == colours[1].lower():             
            score += 1
        e.delete(0, tkinter.END) 
        random.shuffle(colours) 
        label.config(fg = str(colours[1]), text = str(colours[0])) 
        scoreLabel.config(text = "Score: " + str(score)) 
def countdown(): 
    global timeleft 
    if timeleft > 0: 
        timeleft -= 1
        timeLabel.config(text = "Time left: "
                               + str(timeleft)) 
        timeLabel.after(1000, countdown) 
root = tkinter.Tk() 
root.title("COLOR GAME") #title of the game
root.geometry("700x400") #size of the game length and breadth wise
instructions = tkinter.Label(root, text = "Type in the colour"
                        "of the words, and not the word text!", 
                                      font = ('Segoe Script', 16))#you can change the font and its size
instructions.pack()
instruction2=tkinter.Label(root,text="""Your options are:Red, Blue, Green, Cyan, Lime, Brown, Purple,
White, Black, Pink, Orange, Yellow""",font=('Mistral',20))#make color changes here also
instruction2.pack()
scoreLabel = tkinter.Label(root, text = "Press enter to start", 
                                      font = ('Segoe Script', 16)) #you can change the font and its size
scoreLabel.pack() 
timeLabel = tkinter.Label(root, text = "Time left: " +
              str(timeleft), font = ('Segoe Script', 16))  #you can change the font and its size
timeLabel.pack() 
label = tkinter.Label(root, font = ('Segoe Script', 60))  #you can change the font and its size
label.pack() 
e = tkinter.Entry(root) 
root.bind('<Return>', startGame) 
e.pack()   
e.focus_set() 
root.mainloop()
