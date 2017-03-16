import os, sys
import tkinter
from PIL import Image, ImageTk

size = 256, 256

root = tkinter.Tk()

window = tkinter.Frame(root)
window.pack()
image = Image.open("img.jpg")				#Abrir Imagen
image.thumbnail(size, Image.ANTIALIAS)		#Cambia el tamaño de la imagen
tkimage = ImageTk.PhotoImage(image)			#Mostrar imagen
tkinter.Label(window, image=tkimage).pack()




root.mainloop()