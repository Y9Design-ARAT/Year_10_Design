import tkinter as tk 

print("Stage 3")

def proccess(*args):


	val = ent_value.get()
	

	#Check to ensure the string of 1's and 0's
	check = check01(val)
	

	if (check == True):
		lab_results.config(text = "VALID INPUT") 
	#if val is valild 
	else:
		lab_results.config(text = "INVALID INPUT") 


	ent_value.delete(0,tk.END)

def remove0(str):

def check01(str):
	num_0 = str.count("0")
	num_1 = str.count("1")

	if num_0 + num_1 == len(str):
		return True
		return False

root = tk.Tk() 

lab_istructions = tk.Label(root, text = "Enter Binary")  
ent_value = tk.Entry(root)
lab_results = tk.Label(root, text = "--")

#configure Widgets

#Add the widgets to the window
lab_istructions.pack()
ent_value.pack()
lab_results.pack()

root.bind("<Return>", proccess)
root.mainloop()