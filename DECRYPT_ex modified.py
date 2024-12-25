# import tkinter module
from tkinter import *
# import other necessery modules
import random
# Vigenère cipher for encryption and decryption
import base64
# creating root object
root = Tk()
# defining size of window
root.geometry("1200x6000")
# setting up the title of window
root.title("Message Decryption")
Tops = Frame(root, width=2000, relief=SUNKEN)
Tops.pack(side=TOP)
f1 = Frame(root, width=1000, relief=SUNKEN)
f1.pack(side=TOP)
# ==============================================
lblInfo = Label(Tops, font=('1942 report', 50, 'bold'),
                text="SECRET MESSAGING",
                fg="orange",bg='Black', bd=10, anchor='w')
lblInfo.grid(row=0, column=0)
# Initializing variables
Msg = StringVar()
key = StringVar()
mode = StringVar()
Result = StringVar()
# labels for the message
lblMsg = Label(f1, font=('1942 report', 14, 'bold'),
               text="MESSAGE",fg='red', bd=14, anchor="w")
lblMsg.grid(row=1, column=1)
# Entry box for the message
txtMsg = Entry(f1, font=('1942 report', 14, 'bold'),
               textvariable=Msg, bd=10, insertwidth=4,
               bg="black",fg='lime' ,justify='right')
txtMsg.grid(row=1, column=2)

# labels for the key
lblkey = Label(f1, font=('1942 report', 14, 'bold'),
               text="KEY",fg='dark green', bd=14, anchor="w")
lblkey.grid(row=2, column=1)
# Entry box for the key
txtkey = Entry(f1, font=('1942 report', 14, 'bold'),
               textvariable=key, bd=10, insertwidth=4,
               bg="black",fg='white', justify='right')
txtkey.grid(row=2, column=2)

# labels for the result
lblResult = Label(f1, font=('1942 report', 14, 'bold'),
                  text="The Result-", fg='Blue',bd=14, anchor="w")
lblResult.grid(row=3, column=1)
# Entry box for the result
txtResult = Entry(f1, font=('1942 report', 14, 'bold'),
                  textvariable=Result, bd=10, insertwidth=4,
                  bg="black",fg='red', justify='right')
txtResult.grid(row=3, column=2)
# Function to decode
def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) -
                     ord(key_c)) % 256)
        dec.append(dec_c)
        print("dec:", dec)
    return "".join(dec)
def Results():
    # print("Message= ", (Msg.get()))
    msg = Msg.get()
    k = key.get()
    m = mode.get()
    Result.set(decode(k, msg))
# exit function
def qExit():
    root.destroy()
# Function to reset the window
def Reset():
    Msg.set("")
    key.set("")
    mode.set("")
    Result.set("")
# Show message button
btnTotal = Button(f1, padx=14, pady=8, bd=14, fg="white",
                  font=('1942 report', 14, 'bold'), width=10,
                  text="Show Message", bg="navy blue",
                  command=Results).grid(row=6, column=2)
# Reset button
btnReset = Button(f1, padx=14, pady=8, bd=14,
                  fg="white", font=('1942 report', 14, 'bold'),
                  width=10, text="Reset", bg="olive",
                  command=Reset).grid(row=7, column=2)
# Exit button
btnExit = Button(f1, padx=14, pady=8, bd=14,
                 fg="white", font=('1942 report', 14, 'bold'),
                 width=10, text="Exit", bg="crimson",
                 command=qExit).grid(row=8, column=2)
# keeps window alive
root.mainloop()
