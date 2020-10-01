
# https://stackoverflow.com/questions/20822553/align-tabs-from-right-to-left-using-ttk-notebook-widget

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.minsize(300, 300)
root.geometry("1000x700")

style = ttk.Style()
style.configure('TNotebook', tabposition='nw') #'nw' as in compass direction
# style.configure('lefttab.TNotebook', tabposition='ws')

planner = ttk.Notebook(root, width=1000, height=650)

# Create the frames of different colours that are 200*200 pixels in dimensions
tab1 = tk.Frame(planner, bg='red', width=200, height=200)
tab2 = tk.Frame(planner, bg='orange', width=200, height=200)
tab3 = tk.Frame(planner, bg='yellow', width=200, height=200)
tab4 = tk.Frame(planner, bg='green', width=200, height=200)
tab5 = tk.Frame(planner, bg='blue', width=200, height=200)


# Add the tabs/frames to the notebook object called "planner" 
planner.add(tab1, text='Stats')
planner.add(tab2, text='Awards')
planner.add(tab3, text='Players')
planner.add(tab4, text="Teams")
planner.add(tab5, text="Events")


# Tabs will be added to the "top" of the "frame"
planner.pack(side=tk.TOP)

root.mainloop()
