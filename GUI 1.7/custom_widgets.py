import tkinter as tk

# Create a main window
root = tk.Tk()
root.title("Tkinter Button Cursor")
root.geometry("500x400")
root.configure(bg="#f0f0f0")

# Create a button widget with custom cursor
button1 = tk.Button(root, text="Hover over me", cursor="hand2", bg="#3498db",  fg="#ffffff", activebackground="#2980b9", activeforeground="#ffffff", )
button2 = tk.Button(root, text="Hover over me", cursor="hand2", bg="#32a852",  fg="#ffffff", activebackground="#1f5e30", activeforeground="#000000", )
button3 = tk.Button(root, text="Hover over me", cursor="hand2", bg="#d14336",  fg="#ffffff", activebackground="#82251d", activeforeground="#1c1c1c", )
# Packs the buttons while adding padding into them 
button1.pack(pady=20)
button2.pack(pady=20)
button3.pack(pady=20)

label1 = tk.Label(root,text="This text is on the west",bg="#e74c3c", fg="#ffffff", font="Impact",anchor="w")
label1.pack(fill="x", padx=10, pady=5)


label1 = tk.Label(root,text="This text is on the east",bg="#32a852", fg="#ffffff", font="Arial",anchor="e")
label1.pack(fill="x", padx=10, pady=5)

label1 = tk.Label(root,text="This text is on the center",bg="#3498db", fg="#ffffff", font="Comfortaa",anchor="center")
label1.pack(fill="x", padx=10, pady=5)

# Run the application
root.mainloop()