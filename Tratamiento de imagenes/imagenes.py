import os, sys
from tkinter import*
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

def saveImage():
    savefile = tkinter.filedialog.asksaveasfile(mode='w',defaultextension=".jpg")
    if savefile:    #Comprueba si se le dío a cancelar.
        image.save(savefile)
    
root.geometry(window_size)
window = tkinter.Frame(root)
window.pack()
image = Image.open("intro.jpg")				#Abrir Imagen
image.thumbnail(size, Image.ANTIALIAS)		#Cambia el tamaño de la imagen
tkimage = ImageTk.PhotoImage(image)			#Mostrar imagen
panel = tkinter.Label(window, image=tkimage)
panel.grid(row=0)
panel2 = tkinter.Label(window, image=tkimage)
panel2.grid(row=0,column=1)
chooseButton = tkinter.Button(window,text="Selecionar Imagen",command=chooseImage).grid(row=1,column=0)
saveButton = tkinter.Button(window,text="Guadar Imagen",command=saveImage).grid(row=1,column=1)
root.mainloop()
