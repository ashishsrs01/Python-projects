import tkinter as tk
from tkinter import messagebox
import time

class CountdownTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Countdown Timer")
        self.root.geometry("300x200")
        
        # Label for instructions
        self.label = tk.Label(root, text="Enter seconds:", font=("Arial", 12))
        self.label.pack(pady=10)
        
        # Entry for input
        self.entry = tk.Entry(root, font=("Arial", 12))
        self.entry.pack(pady=5)
        
        # Button to start
        self.start_button = tk.Button(root, text="Start Timer", command=self.start_timer, font=("Arial", 12))
        self.start_button.pack(pady=10)
        
        # Label to display countdown
        self.timer_label = tk.Label(root, text="", font=("Arial", 20))
        self.timer_label.pack(pady=20)
        
        self.remaining_seconds = 0
    
    def start_timer(self):
        try:
            seconds = int(self.entry.get())
            if seconds <= 0:
                messagebox.showerror("Error", "Please enter a positive number greater than 0!")
                return
            self.remaining_seconds = seconds
            self.start_button.config(state="disabled")
            self.entry.config(state="disabled")
            self.update_timer()
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number!")
    
    def update_timer(self):
        if self.remaining_seconds > 0:
            mins = self.remaining_seconds // 60
            secs = self.remaining_seconds % 60
            timer_display = f"{mins:02d}:{secs:02d}"
            self.timer_label.config(text=timer_display)
            self.remaining_seconds -= 1
            self.root.after(1000, self.update_timer)
        else:
            self.timer_label.config(text="Time's up! ⏰")
            messagebox.showinfo("Timer", "Beep! Beep! Beep!")
            self.start_button.config(state="normal")
            self.entry.config(state="normal")

def main():
    root = tk.Tk()
    app = CountdownTimer(root)
    root.mainloop()

if __name__ == "__main__":
    main()
