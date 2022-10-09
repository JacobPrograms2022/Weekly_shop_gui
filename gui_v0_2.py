import tkinter as tk
from tkinter import *
from subprocess import call

def open_py_file():
    for widget in display_window.winfo_children():
        widget.destroy()
    #call(["python",r"C:\Users\jacob\Documents\VScode\personal_projects\smite_god_randomizer_2_0\random_god.py"])
    
   
ws = Tk()
ws.title('Next Weeks Shop')
ws.geometry('440x500')
ws.config(bg='black')

img = PhotoImage(file=r"C:\Users\jacob\Documents\VScode\personal_projects\weekly_shop\weekly_shop_gui\images\grocery_image.png")
background = Label(
    ws,
    image=img
)
background.place(x=-220, y=0)


display_window = tk.Frame(
    ws,
    height=180,
    width=310,
  
    bg="light gray"
)
display_window.place(x=0, y=180) # change this (White box)

randomize = Button(
    ws,
    text='Randomize!',
    relief=RAISED,
    font=('Arial Bold', 18),
    fg="white", 
    bg="green",
    command=open_py_file
)
randomize.place(x=390, y=380) # Button Placement
god_text = tk.Label(display_window, height=180,width=420, bg = "light gray")
ws.mainloop()
