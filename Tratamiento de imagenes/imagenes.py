import os, sys
import tkinter
from PIL import Image, ImageTk

size = 256, 256
image = Image.open("img.jpg")				#Abrir Imagen
root = tkinter.Tk()
image.thumbnail(size, Image.ANTIALIAS)		#Cambia el tamaño de la imagen
tkimage = ImageTk.PhotoImage(image)			#Mostrar imagen
tkinter.Label(root, image=tkimage).pack()
root.mainloop()