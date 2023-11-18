import tkinter as tk
import sys
import subprocess
import customtkinter

class ConsoleRedirector:
    def __init__(self, widget):
        self.widget = widget

    def write(self, text):
        self.widget.insert(tk.END, text)
        self.widget.see(tk.END)  # Auto-scroll to the bottom

def run_script():
    # Run your script or command
    script_path = "your_script.py"  # Replace with your script path
    process = subprocess.Popen(["python", script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Redirect stdout and stderr to the console widget
    sys.stdout = ConsoleRedirector(console_text)
    sys.stderr = ConsoleRedirector(console_text)

    # Capture and display the output
    for line in process.stdout:
        print(line, end="")
    for line in process.stderr:
        print(line, end="")

    # Restore stdout and stderr
    sys.stdout = sys.__stdout__
    sys.stderr = sys.__stderr__

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("1280x720")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=10, padx=10, fill="both", expand=True)

# Create a scrolled text widget for displaying the console output
console_text = customtkinter.CTkTextbox(frame, wrap=tk.WORD, width=500, height=500)
console_text.pack(anchor="center", pady=10, padx=10) #Anchor the console box to the middle of the screen and add some padding
console_text.configure(scrollbar_button_color="", scrollbar_button_hover_color="") #Make scroll-bar invisible
font_spec = ("Cascadia Code", 12)  # Font family and size

# Create a button to run the script
run_button = tk.Button(root, text="Run Script", command=run_script)
run_button.pack()

# Start the Tkinter event loop
root.mainloop()
