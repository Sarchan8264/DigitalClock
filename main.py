from tkinter import *
from time import *

w=Tk()
w.title("Digital clock")
w.geometry("450x250")
w.resizable(1,1)

l=Label(w, font=("times new roman" ,68,  "bold") , bg="black", fg="orange")
l.pack()
def update():
    t=strftime("%B:%Y:%A:%H:%M:%S")
    l.config(text=t)
    w.after(1000,update)



update()
w.mainloop()