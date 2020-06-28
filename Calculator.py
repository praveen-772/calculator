#   Calculator using Tkinter

from tkinter import *

expression = ""


def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)


def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set("Error")
        expression = ""


def clear():
    global expression
    expression = ""
    equation.set(expression)


if __name__ == "__main__":
    gui = Tk()
    gui.title(" !!! Calculator in Python by Praveen !!! ")
    gui.geometry("360x400")
    gui.configure(background="#dabbb4")

    equation = StringVar()
    expression_field = Entry(gui, textvariable=equation)
    expression_field.grid(columnspan=8, ipadx=100)
    equation.set('Welcome to My New Calculator Application')

    button1 = Button(gui, text='1', command=lambda: press(1), height=2, width=2)
    button1.grid(row=5, column=0)

    button2 = Button(gui, text='2', command=lambda: press(2), height=2, width=2)
    button2.grid(row=5, column=1)

    button3 = Button(gui, text='3', command=lambda: press(3), height=2, width=2)
    button3.grid(row=5, column=2)

    buttondiv = Button(gui, text='/', command=lambda: press('/'), height=2, width=2)
    buttondiv.grid(row=5, column=3)

    button4 = Button(gui, text='4', command=lambda: press(4), height=2, width=2)
    button4.grid(row=6, column=0)

    button5 = Button(gui, text='5', command=lambda: press(5), height=2, width=2)
    button5.grid(row=6, column=1)

    button6 = Button(gui, text='6', command=lambda: press(6), height=2, width=2)
    button6.grid(row=6, column=2)

    buttonmult = Button(gui, text='X', command=lambda: press('*'), height=2, width=2)
    buttonmult.grid(row=6, column=3)

    button7 = Button(gui, text='7', command=lambda: press(7), height=2, width=2)
    button7.grid(row=7, column=0)

    button8 = Button(gui, text='8', command=lambda: press(8), height=2, width=2)
    button8.grid(row=7, column=1)

    button9 = Button(gui, text='9', command=lambda: press(9), height=2, width=2)
    button9.grid(row=7, column=2)

    buttonmin = Button(gui, text='-', command=lambda: press('-'), height=2, width=2)
    buttonmin.grid(row=7, column=3)

    button0 = Button(gui, text='0', command=lambda: press(0), height=2, width=2)
    button0.grid(row=8, column=0)

    buttondot = Button(gui, text='.', command=lambda: press('.'), height=2, width=2)
    buttondot.grid(row=8, column=1)

    buttonequal = Button(gui, text='=', command=equalpress, height=2, width=2)
    buttonequal.grid(row=8, column=2)

    buttonplus = Button(gui, text='+', command=lambda: press('+'), height=2, width=2)
    buttonplus.grid(row=8, column=3)

    buttonclear = Button(gui, text='C', command=clear, height=2, width=2)
    buttonclear.grid(row=9, column=0)

gui.mainloop()
