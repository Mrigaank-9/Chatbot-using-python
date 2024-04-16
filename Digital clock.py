import tkinter as tk
from tkinter import font
from time import strftime

def update_time():
    current_time = strftime('%I:%M:%S %p')  # Get the current time in 12-hour format
    clock_label.config(text=current_time)  # Update the label text
    clock_label.after(1000, update_time)   # Schedule the update after 1 second

# Create the Tkinter window
root = tk.Tk()
root.title('Digital Clock')
root.geometry('400x200')

# Create a background color gradient
bg_gradient = tk.Canvas(root, width=400, height=200)
bg_gradient.pack(fill='both', expand=True)
bg_gradient.create_rectangle(0, 0, 400, 200, fill='#3498db', outline='')

# Create a custom font for the clock
clock_font = font.Font(family='Arial', size=48, weight='bold')

# Create a label for the clock with rounded corners and gradient text effect
clock_label = tk.Label(bg_gradient, font=clock_font, bg='#3498db', fg='#ffffff', bd=10, relief='solid')
clock_label.place(relx=0.5, rely=0.5, anchor='center')

# Add a subtle animation to the clock label
def animate_clock():
    current_time = strftime('%I:%M:%S %p')  # Get the current time in 12-hour format
    clock_label.config(text=current_time)  # Update the label text
    clock_label.after(1000, animate_clock)  # Schedule the update after 1 second
    # Smooth transition between text color changes
    fg_color = '#ffffff' if clock_label['fg'] == '#ffffff' else '#000000'
    clock_label.config(fg=fg_color)
    # Apply gradient effect to text
    clock_label.config(fg=f'#{int(clock_label.winfo_rgb("#ffffff")[1]):02x}{int(clock_label.winfo_rgb("#3498db")[1]):02x}{int(clock_label.winfo_rgb("#ffffff")[1]):02x}')

# Call the animate_clock function to start the clock with animation
animate_clock()

# Run the Tkinter event loop
root.mainloop()
