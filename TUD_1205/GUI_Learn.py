"""
Different possible libraries

TkInter- Already embedded
Qt5- most popular
wxWidgets
GTK
"""

# ----------------------------------------------------------------------------------------------------------
# TkInter
import tkinter as tk
from tkinter import filedialog  # For a==2


# ----------------------------------------------------------------------------------------------------------
# Function
def calculator():
    # Make the calculations
    operator_ = operator.get()  # Obtain operator and values
    val1 = float(input1.get())
    val2 = float(input2.get())
    if operator_ == '+':
        myres = val1 + val2
        result.set(str(myres))
    if operator_ == '-':
        myres = val1 - val2
        result.set(str(myres))
    if operator_ == '*':
        myres = val1 * val2
        result.set(str(myres))
    if operator_ == '/' and val2 != 0:
        myres = val1 / val2
        result.set(str(myres))
    if operator_ == '/' and val2 == 0:
        result.set('Error')


# ----------------------------------------------------------------------------------------------------------
# Keep code tidy
a = 1

# Create a window
win = tk.Tk()

# Basic window
if a == 1:
    # Give a title
    win.title("My first GUI")

    # Add a text label
    label_1 = tk.Label(win, text="This is a label")
    label_1.grid(column=0, row=0)

    label_2 = tk.Label(win, text="Second label", background="blue")
    label_2.grid(column=0, row=1)  # Can be put on top of previous one

    # Add a button
    button_1 = tk.Button(win, text="This is a button", background="red")
    button_1.grid(column=1, row=0)

    # Add an image
    image1 = tk.PhotoImage(file='./Data/Cowtapult/cow.png')
    label_3 = tk.Label(win, image=image1)
    label_3.grid(column=1, row=1)

    # Set background
    win.configure(bg='white')

# Specific window
if a == 2:
    # Withdraw window to call the dialog window
    win.withdraw()

    # Open file function
    result = filedialog.askopenfilename(title="Open file", filetypes=[('Data types', 'gif'), ('All files', '.*')])
    if result:
        print(f'The selected file is {result}')
    else:
        print('Nothing selected')

# Other standard dialogs
"""
messagebox
    mbox.showinfo()
    mbox.askquestion()
simpledialog
    sd.askstring()
    sd.askfloat()
filedialog
    fd.askfileopen()
    fd.asksavefile()
colorchooser
    cs.askcolor
"""

# Simple calculator
if a == 3:
    myres = 0.0

    # Size
    win.geometry('500x300')
    win.resizable(False, False)

    # Title
    win.title("Basic calculator")

    # Create space for input
    input1 = tk.StringVar(None)
    entry1 = tk.Entry(win, textvariable=input1)
    entry1.grid(column=0, row=0)

    # Draw a menu
    operator = tk.StringVar()
    operator.set('+')  # Default
    operator_menu = tk.OptionMenu(win, operator, '+', '-', '*', '/')  # Crate a menu, attach to window and select ope...
    operator_menu.grid(column=1, row=0)

    input2 = tk.StringVar(None)
    entry2 = tk.Entry(win, textvariable=input2)
    entry2.grid(column=2, row=0)

    # Operations part
    button1 = tk.Button(win, text='=', command=calculator)  # Command is the function called every time you click
    button1.grid(column=3, row=0)

    # Show result in label
    result = tk.StringVar()
    result.set("-")
    label1 = tk.Label(win, textvariable=result)
    label1.grid(column=4, row=0)

# Be sure to do the parts before the loop
# Rendering the content. Equivalent to while running, update
win.mainloop()
