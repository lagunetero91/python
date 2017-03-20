import os, sys
from tkinter import*
import tkinter.filedialog
from copy import copy
from PIL import Image, ImageTk,ImageFilter,ImageOps

window_size= "640x480"      #Tamaño de la ventana del programa.
size = 256, 256             #Tamaño de las miniaturas de las imágenes.

filters = {'Invertir color', 'Normal','Escala de grises'}      #ComboBox: Filtros
root = tkinter.Tk()
tkvar = StringVar(root)
tkvar.set('Invertir color')

# Método que se utiliza para cargar una imagen al programa.
def chooseImage():
    global acI
    filename =tkinter.filedialog.askopenfilename()
    inImage2 = Image.open(filename)				#Abrir Imagen
    acI = copy(inImage2)
    inImage2.thumbnail(size, Image.ANTIALIAS)		#Cambia el tamaño de la imagen
    tkimage2 = ImageTk.PhotoImage(inImage2)			#Mostrar imagen
    panel.configure(image = tkimage2)
    panel.image = tkimage2
    
   
#Método encargado de guardar la imagen procesada.
def saveImage():
    global outI
    savefile = tkinter.filedialog.asksaveasfile(mode='w',defaultextension=".jpg")
    if savefile:    #Comprueba si se le dío a cancelar.
        outI.save(savefile)

#Método encargado de aplicar los filtros.
def aplyFilter():
    global acI
    global outI
    auxiliarImg = copy(acI)
    filter = tkvar.get()
    if filter == 'Invertir color' :
        showIm = ImageOps.invert(auxiliarImg)
        outI=copy(showIm)
        showIm.thumbnail(size, Image.ANTIALIAS)
        tkimageout2 = ImageTk.PhotoImage(showIm)			#Mostrar imagen
        panel2.configure(image = tkimageout2)
        panel2.image = tkimageout2
    elif filter == 'Normal':
        tkimageout2 = ImageTk.PhotoImage(acI)			        #Mostrar imagen
        panel2.configure(image = tkimageout2)
        panel2.image = tkimageout2
    elif filter == 'Escala de grises':
        showIm = acI.convert("L")
        outI=copy(showIm)
        showIm.thumbnail(size, Image.ANTIALIAS)
        tkimageout2 = ImageTk.PhotoImage(showIm)			#Mostrar imagen
        panel2.configure(image = tkimageout2)
        panel2.image = tkimageout2

root.geometry(window_size)
window = tkinter.Frame(root)
window.pack()
inImage = Image.open("intro.jpg")                      #Abrir Imagen por defecto de la entrada.
acI = copy(inImage)
print(id(acI))
outI = copy(inImage)
print(id(outI))
inImage.thumbnail(size, Image.ANTIALIAS)		#Cambia el tamaño de la imagen
tkimage = ImageTk.PhotoImage(inImage)			#Mostrar imagen
panel = tkinter.Label(window, image=tkimage,width=256,height=256)
panel.grid(row=0)

outputimage = Image.open("result.jpg")			#Abrir Imagen por defecto de la salida.
outputimage.thumbnail(size, Image.ANTIALIAS)		#Cambia el tamaño de la imagen
tkimageout = ImageTk.PhotoImage(outputimage)
panel2 = tkinter.Label(window, image=tkimageout,width=256,height=256)
panel2.grid(row=0,column=2)

chooseButton = tkinter.Button(window,text="Selecionar Imagen",command=chooseImage).grid(row=1,column=0,pady=8)      #Botón de carga de imágenes
saveButton = tkinter.Button(window,text="Guadar Imagen",command=saveImage).grid(row=1,column=2)                     #Botón para guardar imágenes
Label(window,text="Seleccione filtro: ").grid(row=2,column=0)
filterMenu = OptionMenu(window,tkvar,*filters).grid(row=2,column=1)                                                 #ComboBox
filerButton = tkinter.Button(window,text="Aplicar Filtro",command=aplyFilter).grid(row=2,column=2,pady= 30)         #Botón que aplica el filtro seleccionado por el ComboBox
root.mainloop()
