import tkinter as tk
from tkinter import CENTER, filedialog, PhotoImage
import os

root = tk.Tk() # Body, holds the structure of the app
apps = []

if os.path.isfile("save.txt"):
    with open("save.txt", "r") as f:
        tempApps = f.read()
        tempApps = tempApps.split(",")
        apps = [x for x in tempApps if x.strip()]

def addApp(): # adds the file directory to the screen
    for widget in frame.winfo_children():
        widget.destroy()
    filename = filedialog.askopenfilename(initialdir="/", title="Select file",
               filetypes=(("executables","*.exe"),("all files", "*.*"))) #file browser

    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg="gray")#pastes the directories to the screen
        label.pack()

def runApps():
    for app in apps:
        os.startfile(app)

canvas = tk.Canvas(root, height=400, width=600, bg="#263D42") # size properties and colour
canvas.pack()
img = PhotoImage(file=r"C:\Users\jacob\Documents\VScode\personal_projects\weekly_shop\weekly_shop_gui\images\grocery_image.png")
background = tk.Label(
    canvas,
    image=img
)
background.place(x=-220, y=0)

frame = tk.Frame(canvas, bg="white")
frame.place(relwidth=0.8, relheight=0.7, relx=0.1, rely=0.1) # creates frame, relx and rely centralize the frame. Width and Heigth take priority over relx and rely.

openFile = tk.Button(frame, text="Open File", padx=10, 
                    pady=5, fg="white", bg="#263D42", command=addApp) #Creates a button

openFile.pack()

runApps = tk.Button(frame, text="Run Apps", padx=10, 
                    pady=5, fg="white", bg="#263D42", command=runApps)
runApps.pack()

for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()

root.mainloop()


with open("save.txt", "w") as f:
    for app in apps:
        f.write(app+",")
