#!/usr/bin/python3
try:
	from Tkinter import*
except ImportError:
	from tkinter import*
	
import tkinter.messagebox
import socket
import time
root = Tk()

def startServer():
	ip = ipCon.get()
	port = portCon.get()
	if len(ip)>0 and len(port)>0:
		cadena = "Ip: "+ip+" Puerto: "+port
		tkinter.messagebox.showinfo("Información",cadena)
		#try:
		connSocket = socket.socket()
		connSocket.bind((str(ip),int(port)))
			
		tkinter.messagebox.showinfo("Información","Conexión establecida con "+ip+":"+port)
		connSocket.listen(1)
		conn,addr = connSocket.accept()
		inText.configure(state='normal')
		inText.insert(INSERT,"Conexión establecida con: "+ str(addr)+"\n")
		inText.configure(state='disable')
		time.sleep(5)	
		
		while True:
			data = conn.recv(1024).decode()
			if not data:
				break
			data = conn.recv(1024).decode()
			inText.configure(state='normal')
			inText.insert(CURRENT,str(data)+"\n")
			inText.configure(state='disable')
		#except:
		#	tkinter.messagebox.showinfo("Información","Imposible establecer la conección.")
	else:
		tkinter.messagebox.showinfo("Información","Introduzca una ip y un puerto válidos.")

def closeServer():
	connSocket.close()


#conection Frame
window = Frame(root)
window.pack()

Label(window,text="IP: ").grid(row=0)
ipCon = Entry(window)
ipCon.grid(row=0,column=1)
Label(window,text="Puerto: ").grid(row=0,column=2,padx=5)
portCon = Entry(window)
portCon.grid(row=0,column=3,padx=5)
createServerButton = Button(window,text="Crear servidor",command=startServer).grid(row=1,column=0,padx=5,pady=10)
closeServerButton = Button(window,text="Cerrar servidor",command=closeServer).grid(row=1,column=3,padx=5,pady=10)

#Data Box
recvText = Frame(root)
recvText.pack()
inText = Text(recvText,height=4,width=35,padx=5)
inText.pack()

window.mainloop()