import tkinter as tk

def pocket():

    def button_click(number):
        button = entry.get()
        entry.delete(0, tk.END)
        entry.insert(0, str(button) + str(number))

    def button_clear():
        entry.delete(0, tk.END)

    def button_backspace():
        button = entry.get()[:-1]
        entry.delete(0, tk.END)
        entry.insert(0, button)

    def button_equal():
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(0, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(0, "Error")

    # Creates the main window
    root = tk.Tk()
    root.title("3.1 Pocket Calculator")

    # Creates entry widget
    entry = tk.Entry(root, width=35, borderwidth=5, font=('Impact', 14))
    entry.grid(row=0, column=0, columnspan=10, padx=10, pady=10)

    # Define buttons
    buttons = [
        ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
        ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
        ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ('⌫', 5, 3)  # Backspace button
    ]

    # Creates and place buttons
    for (text, row, col) in buttons:
        if text == 'C':
            btn = tk.Button(root, text=text, padx=40, pady=20, command=button_clear)
        elif text == '=':
            btn = tk.Button(root, text=text, padx=40, pady=20, command=button_equal)
        elif text == '⌫':
            btn = tk.Button(root, text=text, padx=40, pady=20, command=button_backspace)
        else:
            btn = tk.Button(root, text=text, padx=40, pady=20, command=lambda t=text: button_click(t))
        btn.grid(row=row, column=col)

    # Start the main loop
    root.mainloop()

pocket()