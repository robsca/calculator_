import tkinter as tk

# create a window
window = tk.Tk()

# create a unique entry for the mathematical expression
entry = tk.Entry(window, width = 35,borderwidth=5)
entry.grid(row =0, column = 0, columnspan=3, padx = 10, pady = 10)

# create a function to add the number to the entry
def button_click(number):
    # get the current number to the entry
    current = entry.get()
    # add the new number to the entry
    entry.delete(0, tk.END)
    entry.insert(0, str(current) + str(number))

# create a function to clear the entry
def button_clear():
    # clear all
    entry.delete(0, tk.END)

# create a button for the + - * /
# addition
def button_add():
    # get the entry
    first_number = entry.get()
    # add the +
    entry.delete(0,tk.END)
    entry.insert(0, str(first_number) + '+')

# multiplication
def button_multiply():
    # get the entry
    first_number = entry.get()
    # add the +
    entry.delete(0,tk.END)
    entry.insert(0, str(first_number) + '*')

# division
def button_divide():
    # get the entry
    first_number = entry.get()
    # add the +
    entry.delete(0,tk.END)
    entry.insert(0, str(first_number) + '/')

# subtraction
def button_subtract():
    # get the entry
    first_number = entry.get()
    # add the +
    entry.delete(0,tk.END)
    entry.insert(0, str(first_number) + '-')

# create a button to get the result back
def button_equal():
    # get the expression from entry
    expression = entry.get()
    # use the "eval" function to compute the result from a string to python interpreter
    result = eval(expression)
    # add the result to the entry
    entry.delete(0, tk.END)
    entry.insert(0, result)

# Now we create the button to attach the function to
button_1 = tk.Button(window, text = '1', padx = 40, pady = 20, command=lambda: button_click(1))
button_2 = tk.Button(window, text = '2', padx = 40, pady = 20, command=lambda: button_click(2))
button_3 = tk.Button(window, text = '3', padx = 40, pady = 20, command=lambda: button_click(3))
button_4 = tk.Button(window, text = '4', padx = 40, pady = 20, command=lambda: button_click(4))
button_5 = tk.Button(window, text = '5', padx = 40, pady = 20, command=lambda: button_click(5))
button_6 = tk.Button(window, text = '6', padx = 40, pady = 20, command=lambda: button_click(6))
button_7 = tk.Button(window, text = '7', padx = 40, pady = 20, command=lambda: button_click(7))
button_8 = tk.Button(window, text = '8', padx = 40, pady = 20, command=lambda: button_click(8))
button_9 = tk.Button(window, text = '9', padx = 40, pady = 20, command=lambda: button_click(9))
button_0 = tk.Button(window, text = '0', padx = 40, pady = 20, command=lambda: button_click(0))

# Now the opearation symbols
button_add = tk.Button(window, text = '+', padx = 41, pady = 20, command = button_add)
button_subtract = tk.Button(window, text = '-', padx = 41, pady = 20, command = button_subtract)
button_multiply = tk.Button(window, text = '*', padx = 41, pady = 20, command = button_multiply)
button_divide = tk.Button(window, text = '/', padx = 41, pady = 20, command = button_divide)

# the last two are = and clear button
button_clear = tk.Button(window, text = 'Clear', padx = 79, pady = 20, command = button_clear)
button_equal = tk.Button(window, text = '=', padx = 91, pady = 20, command = button_equal)

# the last step is to place all these buttons in the window
button_1.grid(row =3, column = 0)
button_2.grid(row =3, column = 1)
button_3.grid(row =3, column = 2)

button_4.grid(row =2, column = 0)
button_5.grid(row =2, column = 1)
button_6.grid(row =2, column = 2)

button_7.grid(row =1, column = 0)
button_8.grid(row =1, column = 1)
button_9.grid(row =1, column = 2)

button_0.grid(row =4, column = 0)

button_clear.grid(row =4, column = 1, columnspan = 2)
button_equal.grid(row =5, column = 1, columnspan = 2)

button_add.grid(row =5, column = 0)
button_subtract.grid(row =6, column = 0)
button_multiply.grid(row =6, column = 1)
button_divide.grid(row =6, column = 2)

# run the application
window.mainloop()

'''It's done, let's run it'''