'''
Asher Forman
File Opening GUI
2/22/2021
'''
from tkinter import *
from tkinter import filedialog
import tkinter.scrolledtext as st

master = Tk()
master.title('My File Opener')
master.geometry("500x500")
master.configure(background="blue")

# Dropdown Submenu Example
def closefile():
    print('Closing File')


def openfile():
    print('Opening File')
    openfilename = filedialog.askopenfilename(title="Please select a file to open...", filetypes=(("txt files", "*.txt"),("all files", "*.*")))
    print('Opening file at'+ openfilename)

def submenu():
    menu = Menu(master)
    submenu = Menu(menu)
    master.config(menu=menu)
    menu.add_cascade(label="File", menu=submenu)
    submenu.add_command(label="Open", command=openfile)
    submenu.add_separator()
    submenu.add_command(label="Close", command=closefile)

def show_text_box():
    print("show text box")
    text_box = st.ScrolledText(master, bg = "grey20", font = 'TkFixedFont')
    text_box.insert(INSERT, "inserting")
    text_box.place(x = 100, y = 100, width = 100, height = 100)

def read_file():
    print("read file")

def write_file():
    print("write file")


# Simple Buttons for Interface
Button(master, text="Show Text Box", command = show_text_box, bg = "grey20", highlightbackground = "black", foreground = "blue").grid(row = 0, column = 0)
Button(master, text="Get Text", command = read_file, bg = "grey20", highlightbackground = "black", foreground = "blue").grid(row = 0, column = 1)
Button(master, text="Write Text", command = write_file, bg = "grey20", highlightbackground = "black", foreground = "blue").grid(row = 0, column = 2)


submenu()
master.mainloop()