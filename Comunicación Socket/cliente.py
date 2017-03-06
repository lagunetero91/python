#!/usr/bin/python3
try:
	from Tkinter import*
except ImportError:
	from tkinter import*
	

root = Tk()

#conection Frame
window = Frame(root)
Label(window,text="Datos de conexión")
window.pack()

Label(window,text="IP").grid(row=0)
ipCon = Entry(window)
ipCon.grid(row=0,column=1)
conButton = Button(window,text="Conectar").grid(row=1,column=0,padx=5,pady=10)
endConButton = Button(window,text="Cerrar conexión").grid(row=1,column=3,padx=5,pady=10)

#Data Box
text = Frame(root)
text.pack()
inText = Text(text,height=4).pack()


send = Frame(root)
send.pack()
sendButton = Button(send,text="Enviar").grid(row=1,column=0,padx=5,pady=10)
clearConButton = Button(send,text="Limpiar").grid(row=1,column=3,padx=5,pady=10)
window.mainloop()