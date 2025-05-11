import tkinter as tk

# Create the main window
root = tk.Tk()
root.geometry("400x400")  # Set the window size
root.configure(bg="white")  # Set the initial background color to white

# Function to change the background color to black
def change_color():
    root.configure(bg="#fcba03")

# Schedule the change_color function to be called after 3000 milliseconds (3 seconds)
root.after(1500, change_color)

def changeSize():
    currentSize = root.geometry().split('+')[0]
    if currentSize == "400x400":
        root.geometry("500x800")
    else:
        root.geometry("400x400")

def changeGoodbyeBtn():
    current_txt = goodbye_button.cget("text")
    if current_txt == "Goodbye!":
        goodbye_button.config(text="Adios!")
    else:
        goodbye_button.config(text="Goodbye!")

# Add a button that says "Goodbye!"
goodbye_button = tk.Button(root, text="Goodbye!", command=root.destroy)
goodbye_button.pack(pady=20)

size_button = tk.Button(root, text="Change Window Size", command=changeSize)
size_button.pack(pady=20)

txt_button = tk.Button(root, text="Change Goodbye Text", command=changeGoodbyeBtn)
txt_button.pack(pady=20)
# Set focus on the goodbye button
goodbye_button.focus_set()

# Start the Tkinter event loop
root.mainloop()