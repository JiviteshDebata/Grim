import os
import sys
import subprocess
from tkinter import *
from tkinter import ttk
from tkinter import filedialog


def set_image(path):
    to_write="GRUB_BACKGROUND="+path
    f=open('/etc/default/grub','a+')
    f.write(to_write)

#main window
root=Tk()
root.title("GRIM")
root.geometry("380x120")

def select_image():
    root.filename = filedialog.askopenfilename(title="Select file",filetypes = (("png","*.png"),("All files","*.*")))
    path=root.filename
    set_image(path)

#def download_image()
#def preview_image()

Fline=Label(root,text="This program modifies the grub file in order to function properly")
Sline=Label(root,text="Use at your own risk")
Sel_Img=Button(root ,text="Select Image",command=lambda:select_image())
Dwn_Img=Button(root ,text="Download Image")
Prv_Img=Button(root ,text="Preview Image")

#Allignment
Fline.grid(row=0,pady=2,padx=20,sticky=W)
Sline.grid(row=1,stick=S)
Sel_Img.grid(row=2,padx=20,stick=W)
Dwn_Img.grid(row=2,padx=20,stick=E)
Prv_Img.grid(row=3,column=0,padx=2,pady=10,sticky=S)

root.mainloop()
