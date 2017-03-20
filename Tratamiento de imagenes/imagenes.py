import os, sys
import tkinter
import tkinter.filedialog
from PIL import Image, ImageTk

window_size= "640x480"
size = 256, 256
root = tkinter.Tk()

def chooseImage():
    filename =tkinter.filedialog.askopenfilename()
    print(filename)
    image2 = Image.open(filename)				#Abrir Imagen
    image2.thumbnail(size, Image.ANTIALIAS)		#Cambia el tamaño de la imagen
    tkimage2 = ImageTk.PhotoImage(image2)			#Mostrar imagen
    panel.configure(image = tkimage2)
    panel.image = tkimage2


root.geometry(window_size)
window = tkinter.Frame(root)
window.pack()
image = Image.open("intro.jpg")				#Abrir Imagen
image.thumbnail(size, Image.ANTIALIAS)		#Cambia el tamaño de la imagen
tkimage = ImageTk.PhotoImage(image)			#Mostrar imagen
panel = tkinter.Label(window, image=tkimage)
panel.pack()
chooseButton = tkinter.Button(window,text="Selecionar Imagen",command=chooseImage).pack()
root.mainloop()
