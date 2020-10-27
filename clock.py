#iporting whole module
from tkinter import *
from tkinter.ttk import *

#importing strftime function to retrieve system's time
from time import strftime

#creating tkinter window
root = Tk()
root.title('Clock')

#this function is used to display time on label
def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text = string)
    lbl.after(1000, time)

#styling the label widget so that clock will look more attractive
lbl = Label(root, font = ('calibri', 40, 'bold'),
            background = 'yellow',
            foreground = 'red')

#placing clock at the center of the tkinter window
lbl.pack(anchor = 'center')
time()

mainloop()
