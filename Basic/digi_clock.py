from tkinter import *
from time import strftime
root = Tk()
root.title("Digital Clock")
root.geometry("350x150")
root.configure(bg="white")
def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)
label = Label(root, font=('calibri', 50, 'bold'),background='white', foreground='purple')
label.pack(anchor='center')
time()
root.mainloop()