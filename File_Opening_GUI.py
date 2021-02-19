import tkinter
from tkinter import *
from tkinter import filedialog
import tkinter.scrolledtext as st

master = Tk()
master.title('A Random GUI')
master.geometry("500x500")
master.configure(background="grey30")

# THIS IS A DROPDOWN SUBMENU EXAMPLE
def closefile():
    print('Closing File')


def openfile():
    print('Opening File')
    openfilename = filedialog.askopenfilename(title="Please select a file to open...", filetypes=(("txt files", "*.txt"),("all files", "*.*")))
    print('Opening file at'+openfilename)

def submenu():
    menu = Menu(master)
    submenu = Menu(menu)
    master.config(menu=menu)
    menu.add_cascade(label="File", menu=submenu)
    submenu.add_command(label="Open", command=openfile)
    submenu.add_separator()
    submenu.add_command(label="Close", command=closefile)

submenu()

master.mainloop()