#!/usr/bin/python3
try:
	from Tkinter import*
except ImportError:
	from tkinter import*
	
import tkinter.messagebox
import socket

connSocket = socket.socket()	
root = Tk()

def startConn():
	global connSocket
	ip = ipCon.get()
	port = portCon.get()
	if len(ip)>0 and len(port)>0:
		cadena = "Ip: "+ip+" Puerto: "+port
		tkinter.messagebox.showinfo("Información",cadena)
		try:
			
			connSocket.connect((str(ip),int(port)))
			tkinter.messagebox.showinfo("Información","Conexión establecida con "+ip+":"+port)
		except:
			tkinter.messagebox.showinfo("Información","Imposible establecer la conección.")
	else:
		tkinter.messagebox.showinfo("Información","Introduzca una ip y un puerto válidos.")

def endConn():
	global connSocket
	connSocket.close()

def sendData():
	global connSocket
	
	tkinter.messagebox.showinfo("Información",inText.get(1.0,END))
	connSocket.send(inText.get(1.0,END).encode())

#conection Frame
window = Frame(root)
Label(window,text="Datos de conexión")
window.pack()

Label(window,text="IP: ").grid(row=0)
ipCon = Entry(window)
ipCon.grid(row=0,column=1)
Label(window,text="Puerto: ").grid(row=0,column=2,padx=5)
portCon = Entry(window)
portCon.grid(row=0,column=3,padx=5)
conButton = Button(window,text="Conectar",command=startConn).grid(row=1,column=0,padx=5,pady=10)
endConButton = Button(window,text="Cerrar conexión",command=endConn).grid(row=1,column=3,padx=5,pady=10)

#Data Box
sendText = Frame(root)
sendText.pack()
inText = Text(sendText,height=4,width=35,padx=5)
inText.pack()


send = Frame(root)
send.pack()
sendButton = Button(send,text="Enviar",command=sendData).grid(row=1,column=0,padx=5,pady=10)
clearConButton = Button(send,text="Limpiar").grid(row=1,column=3,padx=5,pady=10)
window.mainloop()