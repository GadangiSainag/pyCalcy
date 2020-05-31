from tkinter import *
from tkinter import filedialog



class Editor():
	def __init__(self, root):
		self.root =root
		self.root.title('TEXT EDITOR')
		self.root.geometry('1200x700')
		self.filename = None
		self.title = StringVar()
		self.status= StringVar()
		self.titlebar=Label(self.root,textvariable=self.title, font =('times new roman', 15,'bold'),bd=2, relief =GROOVE )
		self.titlebar.pack(side=TOP, fill =BOTH)
		self.set_title()
		self.statusbar = Label(self.root, textvariable = self.status, font = ("times new roman", 15),bd=2,relief=GROOVE)
		self.statusbar.pack(side= BOTTOM, fill=BOTH)
		self.status.set('Welcome To Text Editor')

		self.menubar =Menu(self.root, font=('times new roman', 15, 'bold'), activebackground='red')
		self.root.config(menu =self.menubar)

		
		self.filemenu= Menu(self.menubar, font= ('times new roman', 12, 'bold'), activebackground='skyblue',tearoff=0)
		self.menubar.add_cascade(menu=self.filemenu, label ="File")
		self.filemenu.add_command(label= 'New', accelerator= ' Ctrl+N', command= self.newfile)
		self.filemenu.add_command(label= 'Open', accelerator= 'Ctrl+O',  command=self.openfile)
		self.filemenu.add_command(label= 'Save', accelerator= 'Ctrl+S',  command=self.savefile)
		self.filemenu.add_command(label= 'Save As', accelerator= 'Ctrl+Shift+A',  command=self.saveasfile)
		self.filemenu.add_separator()
		self.filemenu.add_command(label= 'Exit', accelerator= 'Ctrl+E',  command=root.quit)


		self.editmenu= Menu(self.menubar, font= ('times new roman', 12, 'bold'), activebackground='skyblue',tearoff=0)
		self.menubar.add_cascade(menu=self.editmenu, label ="Edit")
		self.editmenu.add_command(label= 'Cut', accelerator='Ctrl+X', command= self.cut)
		self.editmenu.add_command(label= 'Copy', accelerator='Ctrl+C', command= self.copy)
		self.editmenu.add_command(label= 'Paste', accelerator='Ctrl+V', command= self.paste)
		self.editmenu.add_separator()
		self.editmenu.add_command(label= 'Undo', accelerator='Ctrl+Z', command= self.undo)


		self.helpmenu= Menu(self.menubar, font= ('times new roman', 12, 'bold'), activebackground='skyblue',tearoff=0)
		self.menubar.add_cascade(menu=self.helpmenu, label ="Help")
		self.helpmenu.add_command(label= 'About', command= self.infoabout)

		self.scroll_y=Scrollbar(self.root, orient=VERTICAL)
		self.txtarea=Text(self.root, yscrollcommand=self.scroll_y.set, font=('times new roman', 15,'bold'), relief =GROOVE)
		self.scroll_y.pack(side=RIGHT, fill= Y)
		self.scroll_y.config(command=self.txtarea.yview)
		self.txtarea.pack(fill= BOTH, expand=1)
		self.shortcuts()
	
	def set_title(self):
		if self.filename:
			self.title.set(self.filename)
		else:
			self.title.set('Untitled')

	def newfile(self,*args):
		self.txtarea.delete("1.0", END)
		self.filename=None
		self.set_title()
		self.status.set("New FIle Created")

	def openfile(self, *args):
		try:
			self.filename= filedialog.askopenfilename(title ="Select File",filetype =(("All Files", "*.*"),("Text Files","*.txt"),("Python Files","*.py")))
			if self.filename:
				infile =open(self.filename,"r")
				self.txtarea.delete("1.o", END)
				for line in infile:
					self.txtarea.insert(END, line)
					infile.close()
					self.set_title()
					self.status.set("Opended Successfully")
		except Exception as e:
			messagebox.showerror("Exception", e)

	def savefile(self, *args):
		try:
			if self.filename:
				data= self.txtarea.get("1.0", END)
				outfile= open(self.filename, "W")
				outfile.write(data)
				outfile.close()
				self.set_title()
				self.status.set("Saved Successfully")
			else:
				self.saveasfile()
		except Exception as e :
			messagebox.showerror("Exception", e)
	def saveasfile(self, *args):
		try:
			untitledfile = filedialog.asksaveasfilename(title = "Save file As",defaultextension=".txt",initialfile = "Untitled.txt",filetypes = (("All Files","*.*"),("Text Files","*.txt"),("Python Files","*.py")))
			data = self.txtarea.get("1.0",END)
			outfile = open(untitledfile, "w")
			outfile.write(data)
			outfile.close()
			self.status.set("saved Successfully")
		except Exception as e:
			messagebox.showerror("Exception", e)
	def exit(self,*args): 
		op = messagebox.askyesno("WARNING","Your Unsaved Data May be Lost!!") 
		if op>0: 
			self.root.destroy() 
		else: 
			return

	def cut(self,*args): 
		self.txtarea.event_generate("<<Cut>>") # Defining Copy Funtion 
	def copy(self,*args):
		self.txtarea.event_generate("<<Copy>>") # Defining Paste Funtion 
	def paste(self,*args): 
		self.txtarea.event_generate("<<Paste>>") # Defining Undo Funtion 
	def undo(self,*args): # Exception handling 
		try: # checking if filename not none 
			if self.filename: # Clearing Text Area 

				self.txtarea.delete("1.0",END) # opening File in read mode 
				infile = open(self.filename,"r") # Inserting data Line by line into text area 
				for line in infile: 
					self.txtarea.insert(END,line) # Closing File 
					infile.close() # Calling Set title 
					self.set_title() # Updating Status 
					self.status.set("Undone Successfully") 
			else: # Clearing Text Area 
				self.txtarea.delete("1.0",END) # Updating filename as None 
				self.filename = None # Calling Set 
				self.set_title() # Updating Status 
				self.status.set("Undone Successfully") 
		except Exception as e: 
			messagebox.showerror("Exception",e)

	def infoabout(self): 
		messagebox.showinfo("About Text Editor","A Simple Text Editor\nCreated using Python.") # Defining shortcuts Funtion 
	def shortcuts(self): # Binding Ctrl+n to newfile funtion 
		self.txtarea.bind("<Control-n>",self.newfile) # Binding Ctrl+o to openfile funtion 
		self.txtarea.bind("<Control-o>",self.openfile) # Binding Ctrl+s to savefile funtion 
		self.txtarea.bind("<Control-s>",self.savefile) # Binding Ctrl+a to saveasfile funtion 
		self.txtarea.bind("<Control-Shift-s>",self.saveasfile) # Binding Ctrl+e to exit funtion 
		self.txtarea.bind("<Control-e>",self.exit) # Binding Ctrl+x to cut funtion 
		self.txtarea.bind("<Control-x>",self.cut) # Binding Ctrl+c to copy funtion 
		self.txtarea.bind("<Control-c>",self.copy) # Binding Ctrl+v to paste funtion 
		self.txtarea.bind("<Control-v>",self.paste) # Binding Ctrl+u to undo funtion 
		self.txtarea.bind("<Control-z>",self.undo)


root=Tk()
Editor(root)




root.mainloop()









