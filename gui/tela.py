from tkinter import *
from tkinter import messagebox
from tkinter import ttk

def testando():
    messagebox.showinfo("Hello There")

root = Tk()
root.title('look time study')
root.geometry("500x500")

button1 = Button(root, text="Ver gráficos", command=testando)
button2 = Button(root, text="Start cronograma")

button1.grid(row=0, column=0)
button2.grid(row=1, column=0)


root.mainloop()
