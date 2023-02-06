import pyshorteners
import tkinter as tk
from tkinter import messagebox
import pyperclip


 # Shortens and Copy's URL
 # so you can just go to browser afterwards

def shorten_url():
    long_url = entry.get()
    shortener = pyshorteners.Shortener()
    short_url = shortener.tinyurl.short(long_url)
    pyperclip.copy(short_url)
    messagebox.showinfo("Your new URL has been copied",short_url)
    

# GUI window setup
root = tk.Tk()
root.title("URL Shortener")
root.geometry("400x150")

label1 = tk.Label(root, text="Enter URL to shorten:")
label1.pack()


entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Shorten URL", command=shorten_url)
button.pack()


root.mainloop()
