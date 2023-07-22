from tkinter import *

import random 

window = Tk()


window.title("TESTING RANDOM FUNCTION")
window.geometry("600x600")

input = Entry(window)
input.place(relx = 0.3 , rely = 0.5 , anchor = CENTER)


guessed_password_label = Label(window)
guessed_password_label.place(relx = 0.4 , rely = 0.5 , anchor =  CENTER)

guessed_password_label['text'] = "Guessed Password" + input.get()

Threed_array = [[['A','B','C','D','E','F','G','H','I','J','K','L','M','O','P' ] ,['Queen' ,'King'] , ['!' ,'@' ,'#' ,'$' , '&']]]

def password():
    x = random.randint(0,14)
    y = random.randint(0,1)
    z = random.randint(0,4)
    guessed_password_label['text'] = array_3d[0][0][x] + array_3d[0][1][y] + array_3d[0][2][z]


btn = Button(window , text = "New Password" , command = password)
btn.place(relx = 0.5 , rely = 0.5 , anchor = CENTER)

window.mainloop()