import tkinter as tk
from tkinter import messagebox

def create_main_window():
    # Create and configure main window
    root = tk.Tk()
    root.title("Shaping Main Window")
    
    # Set window icon 
    root.iconbitmap('sandglass.ico')  
    
    # Set window size and limits
    root.geometry("500x400")
    root.minsize(400, 300)
    root.maxsize(800, 600)
    
    # Define a function to handle window close
    def on_closing():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            root.destroy()
    root.protocol("WM_DELETE_WINDOW", on_closing)
    
    # Create main frame
    main_frame = tk.Frame(root, padx=20, pady=20)
    main_frame.pack(fill=tk.BOTH, expand=True)
    
    # Create buttons for message boxes
    tk.Label(main_frame, text="Message Box Examples", font=('Arial', 14)).pack(pady=10)
    
    # Error message button
    def show_error():
        messagebox.showerror("Error", "An unexpected error occurred!")
    tk.Button(main_frame, text="Show Error", command=show_error, width=20).pack(pady=5)
    
    # Warning message button
    def show_warning():
        messagebox.showwarning("Warning", "This is a warning!")
    tk.Button(main_frame, text="Show Warning", command=show_warning, width=20).pack(pady=5)
    
    # Info message button
    def show_info():
        messagebox.showinfo("Information", "This is the info button!")
    tk.Button(main_frame, text="Show Information", command=show_info, width=20).pack(pady=5)
    
    # Yes/No dialog button
    def show_yesno():
        answer = messagebox.askyesno("Question", "Do you want to proceed?")
        messagebox.showinfo("Response", f"You answered: {'Yes' if answer else 'No'}")
    tk.Button(main_frame, text="Ask Yes/No", command=show_yesno, width=20).pack(pady=5)
    
    # OK/Cancel dialog button
    def show_okcancel():
        answer = messagebox.askokcancel("Confirmation", "Are you sure you want to delete this item?")
        messagebox.showinfo("Response", f"You answered: {'OK' if answer else 'Cancel'}")
    tk.Button(main_frame, text="Ask OK/Cancel", command=show_okcancel, width=20).pack(pady=5)
    
    # Retry/Cancel dialog button
    def show_retrycancel():
        answer = messagebox.askretrycancel("Retry", "Do you want to retry?")
        messagebox.showinfo("Response", f"You answered: {'Retry' if answer else 'Cancel'}")
    tk.Button(main_frame, text="Ask Retry/Cancel", command=show_retrycancel, width=20).pack(pady=5)
    
    # Close button
    tk.Button(main_frame, text="Close Window", command=on_closing, width=20).pack(pady=20)
    
    return root



app = create_main_window()
app.mainloop()