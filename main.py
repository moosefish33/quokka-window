import random
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image

root = Tk()
root.resizable(False, False)
root.title("important info")
root.geometry("600x400")
buttonX = 490
buttonY = 300
img1 = ImageTk.PhotoImage(Image.open("quokka1.png"))
def move_button():
    global buttonX
    buttonX += random.randint(-50,50)
    global buttonY
    buttonY += random.randint(-50,50)
    if buttonX > 490:
        buttonX -= 50
    if buttonX < 0:
        buttonX += 50    
    if buttonY > 300:
        buttonY -= 50
    if buttonY < 0:
        buttonY += 50   
    global btn2
    btn2.place(x = buttonX, y = buttonY)
def redraw_button():
    buttonX = 490
    buttonY = 300

def open_second_window():

    top = Toplevel()
    top.resizable(False, False)
    top.geometry("400x400")
    lbl2 = Label(top, font = ("Helvatical bold", 15), text= "I Knew It, Everyone Likes Quokkas!" ).pack()
    btn3 = Button(top, text="Close window", padx=40, pady=20, bg="green", fg="white", command = top.destroy).pack()
                
    if top.destroy:
        buttonX = 490
        buttonY = 300
        global btn2
        btn2.place(x = buttonX, y = buttonY)
root.geometry("600x400")

lbl = Label(root, font = ("Helvatical bold", 30), text="Do You Like Quokkas?").pack()
img_lbl1 =  Label(root, image = img1).pack()
btn = Button(root, text="Yes", padx=40, pady=20, bg="blue", fg="white", command = open_second_window)
btn.place(x = 0, y = 300)
btn2 = Button(root, text="No",  padx=40, pady=20, bg="red", fg="white", command = move_button)
btn2.place(x = buttonX, y = buttonY)

root.mainloop()