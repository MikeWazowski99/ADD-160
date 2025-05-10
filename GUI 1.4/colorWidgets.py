import tkinter as tk

def on_press(button, pressed_color):
    #Change buttons color when pressed
    button.config(bg=pressed_color)

def on_release(button, normal_color):
    #Restore buttons color when released
    button.config(bg=normal_color)

def create_application():
    # Create main window
    root = tk.Tk()
    root.title("Widgets Buttons")
    root.geometry("300x250")
    
    # Button 1 Red
    btn1_normal = "#eb4034"  # Red
    btn1_pressed = "#FF3333"  # Bright red
    # When button is not being pressed or anything color will be red but when it is pressed it will change to bright red
    btn1 = tk.Button(root, text="Button 1", bg=btn1_normal)
    btn1.grid(row=0, column=0, padx=10, pady=10, ipadx=20, ipady=10)
    # Makes it so that the button will change colors when pressed and released by binding the button to functions
    btn1.bind("<ButtonPress-1>",lambda e: on_release(btn1, btn1_pressed))
    btn1.bind("<ButtonRelease-1>",lambda e: on_release(btn1, btn1_normal))
    
    label1 = tk.Label(root, text="Red Button 1!")
    label1.grid(row=0, column=1, padx=10, pady=10)
    
    # Button 2 Green
    btn2_normal = "#53eb34"  # Green
    btn2_pressed = "#33FF33"  # Bright green
    btn2 = tk.Button(root, text="Button 2", bg=btn2_normal)
    btn2.grid(row=1, column=0, padx=10, pady=10, ipadx=20, ipady=10)
    btn2.bind("<ButtonPress-1>",lambda e: on_press(btn2, btn2_pressed))
    btn2.bind("<ButtonRelease-1>",lambda e: on_release(btn2, btn2_normal))
    
    label2 = tk.Label(root, text="Green Button 2!")
    label2.grid(row=1, column=1, padx=10, pady=10)
    
    # Button 3 Blue
    btn3_normal = "#3474eb"  # Blue
    btn3_pressed = "#3333FF"  # Bright blue
    btn3 = tk.Button(root, text="Button 3", bg=btn3_normal)
    btn3.grid(row=2, column=0, padx=10, pady=10, ipadx=20, ipady=10)
    btn3.bind("<ButtonPress-1>",lambda e: on_press(btn3, btn3_pressed))
    btn3.bind("<ButtonRelease-1>",lambda e: on_release(btn3, btn3_normal))
    
    label3 = tk.Label(root, text="Blue Button 3!")
    label3.grid(row=2, column=1, padx=10, pady=10)
    
    # Run the application
    root.mainloop()


create_application()