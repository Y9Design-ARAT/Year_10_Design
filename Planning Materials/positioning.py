import tkinter

root = tkinter.Tk()

root.minsize(width=300, height=300)
root.maxsize(width=300, height=300)

button1 = tkinter.Button(root, text="Current Data")
button1.place(x=90, y=90, anchor="center")

button2 = tkinter.Button(root, text="Historical Data")
button2.place(x=200, y=90, anchor="center")

root.mainloop()

