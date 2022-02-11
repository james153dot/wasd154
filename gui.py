from tkinter import *

root = Tk()

e = Entry(root, width=30, height =15)
e.insert(0, "Enter your first name: ")
e.place(relx=0.65, rely=0.4, anchor=CENTER)

e2 = Entry(root, width=30, height =15)
e2.insert(0, "Enter your last name: ")
e2.place(relx=0.35, rely=0.4, anchor=CENTER)

def myClick():
    myLabel = Label(root, text=e.get() + e2.get())
    myLabel.pack()

myButton = Button(root, text = "NameWriter", command=myClick, width=30, height=5)
myButton.place(relx=0.5, rely=0.65, anchor=CENTER)

 
root.mainloop()







#myLabel1 = Label(root, text="Hello World").grid(row=0, column=0)
#myLabel2 = Label(root, text="My name is Abhijay Movva").grid(row=8, column=10)
#myLabel1.grid(row=0, column=0)
#myLabel2.grid(row=8, column=10)