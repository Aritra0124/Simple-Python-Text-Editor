import os
from tkinter import *
from tkinter import filedialog
import warning

try:
	root = Tk()
	root.resizable(0, 0)
#	root.iconbitmap(r"favicon.ico")
	root.title("Text Editor")
	scroll = Scrollbar(root)
#	scroll.pack(side = RIGHT, fill = Y)
	text = Text(root, yscrollcommand = scroll.set)
	text.grid(row = 0, column = 0, columnspan = 4)
	scroll.config(command=text.yview)
	lsum = Label(root, text = '<<< Output >>>', background="white")
	lsum.grid(row = 1, column = 0, columnspan = 4)
	output = Text(root, width = 80, height = 10 )
	output.grid(row = 2, column = 0, columnspan = 4)
	menubar = Menu(root)
	statusbar = Label(root, text="V1.0", anchor="e", bg="white")
	statusbar.grid(row = 5, column = 0, columnspan = 4)
	root.configure(bg="white")
	menubar.configure(bg="white")
	k = 0
	root.bind("Text", "<Control-Key-a>")

	def opennew():
		import texteditor.py

	def opent():
		global save, root
		save = filedialog.askopenfilename()
		file1 = open(save, "r", encoding='UTF-8')
		x = file1.read()
		text.insert(END,x)
		root.title(save)
		runb.config(state = "normal")

		file1.close()

	def saveas():
		global text,save
		t = text.get("1.0", "end-1c")
		save = filedialog.asksaveasfilename()
		file1 = open(save, "w+")
		file1.write(t)
		file1.close()

	def save():
		global k
		if k == 0:
			saveas()
			runb.config(state = "normal")
			button1.config(state = "normal")
			k = k + 1
		if k > 0:
			global save,text
			t = text.get("1.0", "end-1c")
			file1 = open(save, "w+")
			file1.write(t)
			file1.close()

	def run():
		global save
		code = "python3 "
		k = str((os.popen(code+save).read()))
		output.insert(END,k)

	def color(x):
		if int(x) == 0:
			root.configure(background="white")
			lsum.configure(bg="white", fg="black")
			menubar.configure(bg="white", fg="black")
			text.configure(bg="white", fg="black")
			output.configure(bg="white", fg="black")
			statusbar.configure(bg="white")

		if int(x) == 1:
			root.configure(background="#7E716F")
			lsum.configure(background="#7E716F", fg="white")
			menubar.configure(bg="#7E716F", fg="white")
			text.configure(bg="#DAD7D6", fg="black")
			output.configure(bg="#DAD7D6", fg="black")
			statusbar.configure(bg="#7E716F")

	def web():
		import webbrowser
		webbrowser.open('http://aritrachakraborty.tk', new=2)

	button1 = Button(root, text = "Save as", state = DISABLED, width = 17,command = saveas)
	button2 = Button(root, text = "Save", width = 17, command = save)
	button3 = Button(root, text = "Open", width = 17, command = opent)
	runb = Button(root, text = "RUN",state = DISABLED, bg = "red", width = 17, command = run)
	button1.grid(column = 0,row = 4)
	button2.grid(column = 1,row = 4)
	button3.grid(column = 2,row = 4)
	runb.grid(column = 3,row = 4)

	filemenu = Menu(menubar,tearoff=0)
	filemenu.add_command(label = "New File", command = opennew)
	filemenu.add_command(label = "Open", command = opent)
	filemenu.add_command(label = "Save", command = save)
	filemenu.add_command(label = "Save as", command = saveas)
	filemenu.add_command(label = "Exit", command = lambda : root.quit())
	menubar.add_cascade(label = "File", menu = filemenu)

	editmenu = Menu(menubar, tearoff = 0)
	editmenu.add_command(label = "Cut")
	editmenu.add_command(label = "Copy")
	editmenu.add_command(label = "Paste")
	menubar.add_cascade(label = "Edit", menu = editmenu)

	runmenu = Menu(menubar, tearoff = 0)
	runmenu.add_command(label = "Run", command = lambda : run())
	runmenu.add_command(label = "Direct Run")
	menubar.add_cascade(label = "Run", menu = runmenu)

	modemenu = Menu(menubar, tearoff=0)
	modemenu.add_command(label="Light", command = lambda : color(0))
	modemenu.add_command(label="Dark", command = lambda : color(1))
	menubar.add_cascade(label="Mode", menu=modemenu)

	about = Menu(menubar, tearoff = 0)
	about.add_command(label="About", command = lambda : web())
	about.add_command(label="Version")
	menubar.add_cascade(label="About", menu=about)
	root.config(menu = menubar)
	root.mainloop()

except Exception as e:
	warning.warning(str(e))
