import tkinter as tk
from tkinter import messagebox
from datetime import datetime

root = tk.Tk()

class InteractiveEventApp:
    def __init__(self, root):
        #Creates the window with the title and size
        self.root = root
        self.root.title("Multi Event GUI")
        self.root.geometry("500x500")
        
        # Initialize variables
        self.bg_colors = ["#eb6134", "#34eb80", "#346eeb", "#92f0ca"]
        self.current_bg = 0
        self.song_lines = [
            "I don't want to lie, that's not me",
            "I just wanna be more than a memory",
            "If you dream about me when you fall asleep",
            "I hope you, I hope you",
            "Remember Me by d4vd"
        ]
        self.current_line = 0
        self.click_count = 0
        
        # Create widgets
        self.create_widgets()
    
    def create_widgets(self):
        # Color Change Button
        self.color_btn = tk.Button(self.root, text="Change Background", command=self.change_background, bg="#4CAF50", fg="white", padx=10, pady=5)
        self.color_btn.pack(pady=10)
        
        # Song Display Button and Label
        self.song_btn = tk.Button(self.root, text="Show Next Song Line", command=self.show_next_line, bg="#2196F3", fg="white", padx=10, pady=5)
        self.song_btn.pack(pady=10)
        
        self.song_label = tk.Label(self.root, text="Click the button to see song lines",wraplength=400,font=("Georgia", 12))
        self.song_label.pack(pady=10)
        
        # Click Counter Button and Label
        self.counter_btn = tk.Button(self.root, text="Click Counter", command=self.count_clicks, bg="#FF9800", fg="white", padx=10, pady=5)
        self.counter_btn.pack(pady=10)
        
        self.counter_label = tk.Label(self.root, text="Clicks: 0",font=("Georgia", 12))
        self.counter_label.pack(pady=10)
        
        # Date/Time Button
        self.datetime_btn = tk.Button(self.root, text="Show Date/Time", command=self.show_datetime, bg="#9C27B0", fg="white", padx=10, pady=5)
        self.datetime_btn.pack(pady=10)
    
    def change_background(self):
        #Cycle through background colors
        self.current_bg = (self.current_bg + 1) % len(self.bg_colors)
        self.root.config(bg=self.bg_colors[self.current_bg])
        
        # Update button colors for better visibility
        for btn in [self.color_btn, self.song_btn, self.counter_btn, self.datetime_btn]:
            btn.config(highlightbackground=self.bg_colors[self.current_bg])
    
    def show_next_line(self):
        #Display next line of the song
        if self.current_line < len(self.song_lines):
            self.song_label.config(text=self.song_lines[self.current_line])
            self.current_line += 1
        else:
            self.song_label.config(text="End of song! Click to start again.")
            self.current_line = 0
    
    def count_clicks(self):
        #Increment and display click count
        self.click_count += 1
        self.counter_label.config(text=f"Clicks: {self.click_count}")
        
        # Change color every 5 clicks
        if self.click_count % 5 == 0:
            self.counter_label.config(fg="blue")
        else:
            self.counter_label.config(fg="black")
    
    def show_datetime(self):
        #Display current date and time in a messagebox
        now = datetime.now()
        dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
        messagebox.showinfo("Current Date/Time", f"The current date and time is:\n{dt_string}")



app = InteractiveEventApp(root)
root.mainloop()