import os
import re
import time
from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import *
from tkinter.filedialog import *

class Notepad: 

	__root = Tk() 

	# default window width and height 
	__thisWidth = 300
	__thisHeight = 300
	__thisTextArea = Text(__root) 
	__thisMenuBar = Menu(__root) 
	__thisFileMenu = Menu(__thisMenuBar, tearoff=0) 
	__thisEditMenu = Menu(__thisMenuBar, tearoff=0) 
	__thisHelpMenu = Menu(__thisMenuBar, tearoff=0) 
	__thisStatsMenu = Menu(__thisMenuBar, tearoff=0)
	
	# To add scrollbar 
	__thisScrollBar = Scrollbar(__thisTextArea)	 
	__file = None

	def __init__(self,**kwargs): 

		# Set icon 
		try: 
				self.__root.wm_iconbitmap("notepad.ico") 
		except: 
				pass

		# Set window size (the default is 300x300) 

		try: 
			self.__thisWidth = kwargs['width'] 
		except KeyError: 
			pass

		try: 
			self.__thisHeight = kwargs['height'] 
		except KeyError:
			pass

		# Set the window text 
		self.__root.title("Untitled - Notepad") 

		# Center the window 
		screenWidth = self.__root.winfo_screenwidth() 
		screenHeight = self.__root.winfo_screenheight() 
	
		# For left-alling 
		left = (screenWidth / 2) - (self.__thisWidth / 2) 
		
		# For right-allign 
		top = (screenHeight / 2) - (self.__thisHeight /2) 
		
		# For top and bottom 
		self.__root.geometry('%dx%d+%d+%d' % (self.__thisWidth, 
											self.__thisHeight, 
											left, top)) 

		# To make the textarea auto resizable 
		self.__root.grid_rowconfigure(0, weight=1) 
		self.__root.grid_columnconfigure(0, weight=1) 

		# Add controls (widget) 
		self.__thisTextArea.grid(sticky = N + E + S + W) 
		
		# To open new file 
		self.__thisFileMenu.add_command(label="New", 
										command=self.__newFile)	 
		
		# To open a already existing file 
		self.__thisFileMenu.add_command(label="Open", 
										command=self.__openFile) 
		
		# To save current file 
		self.__thisFileMenu.add_command(label="Save", 
										command=self.__saveFile)
		self.__thisFileMenu.add_command(label="Save As", command=self.__saveasFile)	 

		# To create a line in the dialog		 
		self.__thisFileMenu.add_separator()										 
		self.__thisFileMenu.add_command(label="Exit", 
										command=self.__quitApplication) 
		self.__thisMenuBar.add_cascade(label="File", 
									menu=self.__thisFileMenu)	 
		
		# To give a feature of cut 
		self.__thisEditMenu.add_command(label="Cut", 
										command=self.__cut)			 
	
		# to give a feature of copy	 
		self.__thisEditMenu.add_command(label="Copy", 
										command=self.__copy)		 
		
		# To give a feature of paste 
		self.__thisEditMenu.add_command(label="Paste", 
										command=self.__paste)

		self.__thisEditMenu.add_command(label="Find", command=self.__find)
		self.__thisEditMenu.add_command(label="Find & Replace", command=self.__findReplace) 
		
		# To give a feature of editing 
		self.__thisMenuBar.add_cascade(label="Edit", 
									menu=self.__thisEditMenu)	 
		
		# To create a feature of description of the notepad 
		self.__thisHelpMenu.add_command(label="About Notepad", 
										command=self.__showAbout) 
		self.__thisMenuBar.add_cascade(label="Help", 
									menu=self.__thisHelpMenu) 
		self.__thisStatsMenu.add_command(label="Word Count", command=self.__wordcount)
		self.__thisStatsMenu.add_command(label="Char Count", command=self.__charcount)
		self.__thisStatsMenu.add_command(label="Created Time", command=self.__createdtime)
		self.__thisStatsMenu.add_command(label="Modified Time", command=self.__modifiedtime)

		self.__thisMenuBar.add_cascade(label="Stats", menu=self.__thisStatsMenu)

		self.__root.config(menu=self.__thisMenuBar) 

		self.__thisScrollBar.pack(side=RIGHT,fill=Y)					 
		
		# Scrollbar will adjust automatically according to the content		 
		self.__thisScrollBar.config(command=self.__thisTextArea.yview)	 
		self.__thisTextArea.config(yscrollcommand=self.__thisScrollBar.set) 
	
		
	def __quitApplication(self): 
		self.__root.destroy() 
		# exit() 

	def __showAbout(self): 
		showinfo("Notepad","Soham Roy") 

	def __openFile(self): 
		
		self.__file = askopenfilename(defaultextension=".txt", 
									filetypes=[("All Files","*.*"), 
										("Text Documents","*.txt")]) 

		if self.__file == "": 
			
			# no file to open 
			self.__file = None
		else: 
			
			# Try to open the file 
			# set the window title 
			self.__root.title(os.path.basename(self.__file) + " - Notepad") 
			self.__thisTextArea.delete(1.0,END) 

			file = open(self.__file,"r") 

			self.__thisTextArea.insert(1.0,file.read()) 

			file.close() 

		
	def __newFile(self): 
		self.__root.title("Untitled - Notepad") 
		self.__file = None
		self.__thisTextArea.delete(1.0,END) 

	def __saveFile(self): 

		if self.__file == None: 
			# Save as new file 
			self.__file = asksaveasfilename(initialfile='Untitled.txt', 
											defaultextension=".txt", 
											filetypes=[("All Files","*.*"), 
												("Text Documents","*.txt")]) 

			if self.__file == "": 
				self.__file = None
			else: 
				
				# Try to save the file 
				file = open(self.__file,"w") 
				file.write(self.__thisTextArea.get(1.0,END)) 
				file.close() 
				
				# Change the window title 
				self.__root.title(os.path.basename(self.__file) + " - Notepad") 
				
			
		else: 
			file = open(self.__file,"w") 
			file.write(self.__thisTextArea.get(1.0,END)) 
			file.close() 

	def __saveasFile(self):
		initfile = 'Untitled.txt' if not self.__file else os.path.basename(self.__file)
		self.__file = asksaveasfilename(initialfile=initfile, defaultextension='.txt', filetypes=[('All files', '*.*'), ('Text Documents', '*.txt')])
		if self.__file == "":
			self.__file = None
		else:
			file = open(self.__file, 'w')
			file.write(self.__thisTextArea.get(1.0, END))
			file.close()
			self.__root.title(os.path.basename(self.__file) + ' - Notepad')


	def __cut(self): 
		self.__thisTextArea.event_generate("<<Cut>>") 

	def __copy(self): 
		self.__thisTextArea.event_generate("<<Copy>>") 

	def __paste(self): 
		self.__thisTextArea.event_generate("<<Paste>>") 

	def __find(self):
		global top
		top = Toplevel()
		top.title('Find..')
		top.wm_iconbitmap("notepad.ico")
		e = Entry(top, width=50)
		e.pack(padx=10, pady=10)
		bt1 = Button(top, text='Find', command=lambda :self.find_helper(e.get()))
		bt1.pack(side='right', padx=10, pady=10)
		bt2 = Button(top, text='Cancel', command=self.__cancelfind)
		bt2.pack(side='left', padx=10, pady=10)

	def find_helper(self, txt):
		if txt:
			idx = '1.0'
			while 1: 
				#searches for desried string from index 1 
				idx = self.__thisTextArea.search(txt, idx, nocase=1,  
								stopindex=END)
				if not idx: break

				#last index sum of current index and 
				#length of text 
				lastidx = '%s+%dc' % (idx, len(txt))  

				#overwrite 'Found' at idx 
				self.__thisTextArea.tag_add('found', idx, lastidx)  
				idx = lastidx
			self.__thisTextArea.tag_config('found', foreground='red', background='yellow')

	def __cancelfind(self):
		self.__thisTextArea.tag_remove('found', 1.0, END)
		top.destroy()

	def __findReplace(self):
		global top
		top = Toplevel()
		top.title("Find & Replace")
		top.wm_iconbitmap("notepad.ico")
		lb1 = Label(top, text='Find', padx=10, pady=10)
		lb1.grid(row=0, column=0)
		efind = Entry(top, width=50)
		efind.grid(row=0, column=1, padx=10, pady=10)

		lb2 = Label(top, text="Replace With", padx=10, pady=10)
		lb2.grid(row=1, column=0)
		erep = Entry(top, width=50)
		erep.grid(row=1, column=1, padx=10, pady=10)

		bt = Button(top, text="Find & Replace", command=lambda :self.__replace(efind.get(), erep.get()))
		bt.grid(row=2, column=2, padx=10, pady=10)
		bt2 = Button(top, text='Exit', command=self.__cancelfind)
		bt2.grid(row=2, column=0, padx=10, pady=10)
	
	def __replace(self, txt, rep):
		if txt:
			idx = '1.0'
			idx = self.__thisTextArea.search(txt, idx, stopindex=END)
			lastidx = '%s+%dc' % (idx, len(txt))

			self.__thisTextArea.delete(idx, lastidx)
			self.__thisTextArea.insert(idx, rep)
			lastidx = '%s+%dc' % (idx, len(rep))

			self.__thisTextArea.tag_add('found', idx, lastidx)
			self.__thisTextArea.tag_config('found', foreground='green', background='white')

	def __wordcount(self):
		txt = self.__thisTextArea.get(1.0, END)
		count = len(re.findall(r'(\w+)', txt))
		showinfo("Word Count", "Total Word Count is " + str(count))

	def __charcount(self):
		txt = self.__thisTextArea.get(1.0, END)
		showinfo("Char Count", "Total Char Count is " + str(len(txt)-1))

	def __createdtime(self):
		message = None
		if self.__file:
			message = "Created: %s" % time.ctime(os.path.getctime(self.__file))
		else:
			message = "File is not created yet"
		showinfo("Create Time", message)

	def __modifiedtime(self):
		message = None
		if self.__file:
			message = "Last modified: %s" % time.ctime(os.path.getmtime(self.__file))
		else:
			message = "File is not created yet"
		showinfo("Modified Time", message)

	def run(self): 

		# Run main application 
		self.__root.mainloop() 


# Run main application 
notepad = Notepad(width=600,height=400) 
notepad.run() 
