import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("2.5 Christmas Tree Canvas")

# Create a canvas
canvas = tk.Canvas(root, width=400, height=500, bg='white', borderwidth=2)
canvas.pack()

# Draws the tree (triangles)
canvas.create_polygon(200, 50, 350, 350, 50, 350, outline='dark green', fill='dark green', width=2)
canvas.create_polygon(200, 100, 300, 325, 100, 325, outline='dark green', fill='dark green', width=2)
canvas.create_polygon(200, 150, 250, 300, 150, 300, outline='dark green', fill='dark green', width=2)

# Draws the trunk (rectangle)
canvas.create_rectangle(175, 350, 225, 450, outline='brown4', fill='brown4', width=2)

# Draws ornaments (circles)
canvas.create_oval(200-15, 150-15, 200+15, 100+15, outline='black', fill='red', width=2)        # Top center
canvas.create_oval(170-12, 150-12, 170+12, 150+12, outline='black', fill='yellow', width=2)    # Left middle
canvas.create_oval(250-12, 150-12, 200+12, 150+12, outline='black', fill='yellow', width=2)    # Right middle
canvas.create_oval(150-10, 200-10, 150+10, 200+10, outline='black', fill='blue', width=2)   # Lower left
canvas.create_oval(250-10, 200-10, 250+10, 200+10, outline='black', fill='blue', width=2)   # Lower right
canvas.create_oval(200-14, 220-14, 200+14, 220+14, outline='black', fill='red', width=2)      # Center
canvas.create_oval(170-12, 280-12, 170+12, 280+12, outline='black', fill='orange', width=2)    # Left bottom
canvas.create_oval(230-12, 280-12, 230+12, 280+12, outline='black', fill='orange', width=2)    # Right bottom
canvas.create_oval(140-10, 320-10, 140+10, 320+10, outline='black', fill='white', width=2)     # Far left
canvas.create_oval(260-10, 320-10, 260+10, 320+10, outline='black', fill='white', width=2)     # Far right

# Draws star on top
star_points = [200, 30, 210, 60, 240, 60, 215, 80, 225, 110, 200, 90, 175, 110, 185, 80, 160, 60, 190, 60]
canvas.create_polygon(star_points, outline='gold', fill='gold', width=2)

# Add text
canvas.create_text(200, 480, text="Happy Holidays!", font=('Arial', 24, 'bold'), fill='black')

root.mainloop()