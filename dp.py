import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import os
import shutil

# Function to allow the user to download the file
def download_file():
    # Get the path to the directory where the executable is located
    current_directory = os.path.dirname(os.path.abspath(__file__))
    
    # Path to your Word document
    word_file_path = os.path.join(current_directory, "sample.docx")

    if not os.path.isfile(word_file_path):
        messagebox.showerror("Error", "File not found!")
        return

    # Ask the user where to save the file
    save_path = filedialog.asksaveasfilename(defaultextension=".docx",
                                               filetypes=[("Word documents", "*.docx")])
    
    if save_path:
        # Copy the file to the selected location
        shutil.copy(word_file_path, save_path)
        messagebox.showinfo("Success", "File downloaded successfully!")

# Create the main window
root = tk.Tk()
root.title("Download Word Document")

# Create a button to trigger the download
download_button = tk.Button(root, text="Download Word Document", command=download_file)
download_button.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
