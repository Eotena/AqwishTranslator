# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from tkinter import *

alphabet = "qwertyuiopasdfghjklzxcvbnm"
caps = "QWERTYUIOPASDFGHJKLZXCVBNM"


# Translates the input from the left box, and outputs the result in the right box
def translate():
    translation = encode(var.get())
    var1.set(translation)

# Translates the input from the left box, and outputs the result in the right box
def reverse_translate():
    translation = uncode(var1.get())
    var.set(translation)

# Iterates either convert or capitals or nothing over the input text
def encode(text):
    return ''.join([convert(x, alphabet) if x in alphabet else convert(x, caps) if x in caps else x for x in text])

# Iterates either convert or capitals or nothing over the input text
def uncode(text):
    return ''.join([devert(x, alphabet) if x in alphabet else devert(x, caps) if x in caps else x for x in text])


# Converts letters to the letter two left of it on the keyboard
def convert(letter, dictionary):
    return dictionary[(dictionary.index(letter) - 2) % len(dictionary)]

def devert(letter, dictionary):
    return dictionary[(dictionary.index(letter) + 2) % len(dictionary)]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Tkinter root Window with title
    root = Tk()
    root.title("Translator")

    # Creating a Frame and Grid to hold the Content
    mainframe = Frame(root)
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)
    mainframe.pack(pady=100, padx=100)

    # Text Box to take user input
    Label(mainframe, text="Enter text").grid(row=2, column=0)
    var = StringVar()
    textbox = Entry(mainframe, textvariable=var).grid(row=2, column=1)

    # textbox to show output
    # label can also be used
    Label(mainframe, text="Output").grid(row=2, column=2)
    var1 = StringVar()
    textbox = Entry(mainframe, textvariable=var1).grid(row=2, column=3)

    # creating a button to call Translator function
    b = Button(mainframe, text='Translate', command=translate).grid(row=3, column=0, columnspan=3)

    b = Button(mainframe, text='Reverse translate', command=reverse_translate).grid(row=3, column=2, columnspan=3)

    root.mainloop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

