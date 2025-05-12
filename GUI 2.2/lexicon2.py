import tkinter as tk

def update_label():
    """Retrieve text from Entry and display it in the Label"""
    display_var.set(entry.get())

# Create main window
root = tk.Tk()
root.title("GUI 2.2 Widgets")
root.geometry("500x500")

# Create a Frame widget
main_frame = tk.Frame(root, padx=20, pady=20)
main_frame.pack(padx=10, pady=10)

# Create a LabelFrame widget
label_frame = tk.LabelFrame(main_frame, text="2.2 Widget Work", padx=10, pady=10)
label_frame.pack(padx=10, pady=10)

# Regular Label widget
label = tk.Label(label_frame, text="This is a regular Label Widget:")
label.pack(anchor=tk.W, pady=(0, 5))

# Message widget that auto-wraps text
message = tk.Message(label_frame, text="This is a Message Widget that wraps longer text. " \
                    "Message widgets are good for displaying multiline text that needs to be wrapped at a certain width.", width=300)
message.pack(anchor=tk.W, pady=(0, 10))

# Entry widget with a Label
entry_label = tk.Label(label_frame, text="Enter some text:")
entry_label.pack(anchor=tk.W, pady=(10, 5))

entry = tk.Entry(label_frame, width=50)
entry.pack(anchor=tk.W, pady=(0, 15))

# Button that updates the display label
update_btn = tk.Button(label_frame, text="Update Display", command=update_label)
update_btn.pack(anchor=tk.W, pady=(0, 15))

# Label that will display the Entry text using textvariable
display_var = tk.StringVar()
display_var.set("Text will be displayed here:")
display_label = tk.Label(label_frame, textvariable=display_var, relief=tk.SUNKEN, width=35, anchor=tk.W, padx=10, pady=10)
display_label.pack(anchor=tk.W, fill=tk.X)

# Run the application
root.mainloop()