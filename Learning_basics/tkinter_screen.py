#this how due to Tkinter we can get a size of the screen
import tkinter as tk
root = tk.Tk()
screen_width = root.winfo_screenwidth() #here we get size of user screen
screen_height = root.winfo_screenheight()
print(f'User configs: height - {screen_height} ; width - {screen_width}')
root.destroy()

