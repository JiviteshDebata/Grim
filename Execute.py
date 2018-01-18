from tkinter import *
from tkinter import ttk

#def select_image()
#def download_image()
#def preview_image()

root=Tk()#main window
root.title("GRIM")

Fline=Label(root,text="This program modifies the grub file in order to function properly")
Sline=Label(root,text="Use at your own risk")
Sel_Img=Button(root ,text="Select Image")
Dwn_Img=Button(root ,text="Download Image")
Prv_Img=Button(root ,text="Preview Image")

#Allignment
Fline.grid(row=0,pady=2,padx=20,sticky=W)
Sline.grid(row=1,stick=S)
Sel_Img.grid(row=2,padx=20,stick=W)
Dwn_Img.grid(row=2,padx=1,stick=E)
Prv_Img.grid(row=3,column=0,padx=2,sticky=S)

#Event Handlers(Mouse Button 1 only)
#Sel_Img.bind("<Button-1",select_image)
#Dwn_Img.bind("<Button-1",download_image)
#Prv_Img.bind("<Button-1",preview_image)
