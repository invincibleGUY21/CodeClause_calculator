from tkinter import *
import tkinter.font as font

expression = ""

#Function to update expression
def press(num):
    global expression
    expression = expression + str(num)

    equation.set(expression)

def evaluate():
    try:
        global expression
        total = str(eval(expression))

        equation.set(total)

        expression = ""

    except:
        equation.set("error")
        expression = ""

def clearall():
    global expression
    expression = ""
    equation.set("")



if __name__ == "__main__":
    window = Tk()

    window.configure(background = "black")
    window.title("Calculator")
    window.geometry("530x1000")

    equation = StringVar()

    display = Entry(window, textvariable = equation, font = "Arial 30")

    display.grid(columnspan = 4, ipadx = 50)

    button_font = font.Font(size = 15)

    button1 = Button(window, text=' 1 ', fg='black', bg='grey',
                    command=lambda: press(1), height=5, width=5, font = button_font)
    button1.grid(row=2, column=0)
 
    button2 = Button(window, text=' 2 ', fg='black', bg='grey',
                    command=lambda: press(2), height=5, width=5, font = button_font)
    button2.grid(row=2, column=1)
 
    button3 = Button(window, text=' 3 ', fg='black', bg='grey',
                    command=lambda: press(3), height=5, width=5, font = button_font)
    button3.grid(row=2, column=2)
 
    button4 = Button(window, text=' 4 ', fg='black', bg='grey',
                    command=lambda: press(4), height=5, width=5, font = button_font)
    button4.grid(row=3, column=0)
 
    button5 = Button(window, text=' 5 ', fg='black', bg='grey',
                    command=lambda: press(5), height=5, width=5, font = button_font)
    button5.grid(row=3, column=1)
 
    button6 = Button(window, text=' 6 ', fg='black', bg='grey',
                    command=lambda: press(6), height=5, width=5, font = button_font)
    button6.grid(row=3, column=2)
 
    button7 = Button(window, text=' 7 ', fg='black', bg='grey',
                    command=lambda: press(7), height=5, width=5, font = button_font)
    button7.grid(row=4, column=0)
 
    button8 = Button(window, text=' 8 ', fg='black', bg='grey',
                    command=lambda: press(8), height=5, width=5, font = button_font)
    button8.grid(row=4, column=1)
 
    button9 = Button(window, text=' 9 ', fg='black', bg='grey',
                    command=lambda: press(9), height=5, width=5, font = button_font)
    button9.grid(row=4, column=2)
 
    button0 = Button(window, text=' 0 ', fg='black', bg='grey',
                    command=lambda: press(0), height=5, width=5, font = button_font)
    button0.grid(row=5, column=0)
 
    plus = Button(window, text=' + ', fg='black', bg='grey',
                command=lambda: press("+"), height=5, width=5, font = button_font)
    plus.grid(row=2, column=3)
 
    minus = Button(window, text=' - ', fg='black', bg='grey',
                command=lambda: press("-"), height=5, width=5, font = button_font)
    minus.grid(row=3, column=3)
 
    multiply = Button(window, text=' * ', fg='black', bg='grey',
                    command=lambda: press("*"), height=5, width=5, font = button_font)
    multiply.grid(row=4, column=3)
 
    divide = Button(window, text=' / ', fg='black', bg='grey',
                    command=lambda: press("/"), height=5, width=5, font = button_font)
    divide.grid(row=5, column=3)
 
    equal = Button(window, text=' = ', fg='black', bg='grey',
                command=evaluate, height=5, width=5, font = button_font)
    equal.grid(row=5, column=2)
 
    clear = Button(window, text='Clear', fg='black', bg='grey',
                command=clearall, height=5, width=5, font = button_font)
    clear.grid(row=5, column='1')
 
    Decimal= Button(window, text='.', fg='black', bg='grey',
                    command=lambda: press('.'), height=5, width=5, font = button_font)
    Decimal.grid(row=6, column=0)

    window.mainloop()
    

