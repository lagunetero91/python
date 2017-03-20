import os, sys
from tkinter import*
import tkinter.filedialog

from PIL import Image, ImageTk,ImageFilter,ImageOps

window_size= "640x480"
size = 256, 256
root = tkinter.Tk()


def chooseImage():
    global acI
    filename =tkinter.filedialog.askopenfilename()
    print(filename)
    inImage2 = Image.open(filename)				#Abrir Imagen
    inImage2.thumbnail(size, Image.ANTIALIAS)		#Cambia el tamaño de la imagen
    tkimage2 = ImageTk.PhotoImage(inImage2)			#Mostrar imagen
    panel.configure(image = tkimage2)
    panel.image = tkimage2
    acI = inImage2
   

def saveImage():
    global outI
    savefile = tkinter.filedialog.asksaveasfile(mode='w',defaultextension=".jpg")
    if savefile:    #Comprueba si se le dío a cancelar.
        outI.save(savefile)

def aplyFilter():
    global acI
    global outI
    auxiliarImg = acI
    showIm = ImageOps.invert(auxiliarImg)
    outI=showIm
    tkimageout2 = ImageTk.PhotoImage(showIm)			#Mostrar imagen
    panel2.configure(image = tkimageout2)
    panel2.image = tkimageout2

root.geometry(window_size)
window = tkinter.Frame(root)
window.pack()
inImage = Image.open("intro.jpg")#Abrir Imagen
acI = inImage
outI = inImage
inImage.thumbnail(size, Image.ANTIALIAS)		#Cambia el tamaño de la imagen
tkimage = ImageTk.PhotoImage(inImage)			#Mostrar imagen
panel = tkinter.Label(window, image=tkimage)
panel.grid(row=0)
outputimage = Image.open("result.jpg")				#Abrir Imagen
outputimage.thumbnail(size, Image.ANTIALIAS)		#Cambia el tamaño de la imagen
tkimageout = ImageTk.PhotoImage(outputimage)
panel2 = tkinter.Label(window, image=tkimageout)
panel2.grid(row=0,column=1)
chooseButton = tkinter.Button(window,text="Selecionar Imagen",command=chooseImage).grid(row=1,column=0)
saveButton = tkinter.Button(window,text="Guadar Imagen",command=saveImage).grid(row=1,column=1)
filerButton = tkinter.Button(window,text="Aplicar Filtro",command=aplyFilter).grid(row=2,column=0,pady= 30)
root.mainloop()
