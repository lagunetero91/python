#!/usr/bin/python3
try:
	from Tkinter import*
except ImportError:
	from tkinter import*
	

root = Tk()
window = Frame(root)
window.pack()
Label(window,text="IP").grid(row=0)
ipCon = Entry(window)
ipCon.grid(row=0,column=1)
conButton = Button(window,text="Conectar").grid(row=1,column=0,padx=5,pady=10)
endConButton = Button(window,text="Cerrar conexión").grid(row=1,column=3,padx=5,pady=10)

text = Frame(root)
text.pack()
inText = Text(text,height=4).pack()
#frame = Frame(window)
#frame.pack(fill=BOTH)
#conButton = Button(frame,text="Conectar")
#endConButton = Button(frame,text="Cerrar conexión")

#conButton.pack(side = LEFT)
#endConButton.pack(side = RIGHT)
window.mainloop()