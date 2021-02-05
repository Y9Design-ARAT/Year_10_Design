import tkinter as tk
#Defining option list
OptionList = [
"Stats",
"Awards",
"Players",
"Teams",
]
app = tk.Tk()
#Font and orientation setup
app.geometry('100x200')
variable = tk.StringVar(app)
variable.set(OptionList[0])
opt = tk.OptionMenu(app, variable, *OptionList)
opt.config(width=90, font=('Helvetica', 12))
opt.pack(side="top")
#Label
labelTest = tk.Label(text="", font=('Helvetica', 12), fg='red')
labelTest.pack(side="top")
#Function
def callback(*args):
    labelTest.configure(text="The selected item is {}".format(variable.get()))
variable.trace("w", callback)
app.mainloop()