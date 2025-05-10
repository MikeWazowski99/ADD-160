import tkinter as tk


def creatForm():
    root = tk.Tk()
    root.title("Registration Form")
    root.geometry("300x150")
    
    #Grid layout
    tk.Label(root, text="Name:").grid(row=0, column=0)
    tk.Label(root, text="Email:").grid(row=1, column=0)
    tk.Label(root, text="Password:").grid(row=2, column=0)

    #Entry Fields
    name_entry = tk.Entry(root)
    name_entry.grid(row=0, column=1)

    email_entry = tk.Entry(root)
    email_entry.grid(row=1, column=1)

    password_entry = tk.Entry(root) 
    password_entry.grid(row=2, column=1)
    #Simple Submit button
    submit_button = tk.Button(root, text="Submit")
    submit_button.grid(row=3, column=1)
                    
    root.mainloop()

creatForm()