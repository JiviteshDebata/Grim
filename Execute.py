#!/usr/bin/env python

import os
import sys
import subprocess
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import Image

if os.geteuid() != 0:
    os.execvp("sudo", ["sudo"]+["python3"] + sys.argv) #To check root priviledges


path=""
def set_image(data):
    to_write="GRUB_BACKGROUND="+data
    f=open('/etc/default/grub','a+')
    f.write(to_write)
    f.close()

def select_image():
    global path
    root.filename = filedialog.askopenfilename(title="Select file",filetypes = (("png","*.png"),("All files","*.*")))
    path=root.filename
    set_image(path)

#def download_image()
def preview_image():
    global path
    if(path==""):
        window=Toplevel(root)
        NALINE=Label(window,text="No image has been selected")
        NALINE.pack()
    else:
        img=Image.open(path)
        img.show()

#main window
root=Tk()
root.title("GRIM")
root.geometry("420x120")

Fline=Label(root,text="This program modifies the grub file in order to function properly")
Sline=Label(root,text="Use at your own risk")
Sel_Img=Button(root ,text="Select Image",command=lambda:select_image())
Dwn_Img=Button(root ,text="Download Image")
Prv_Img=Button(root ,text="Preview Image",command=lambda:preview_image())

#Allignment
Fline.grid(row=0,pady=2,padx=20,sticky=W)
Sline.grid(row=1,stick=S)
Sel_Img.grid(row=2,padx=20,stick=W)
Dwn_Img.grid(row=2,padx=20,stick=E)
Prv_Img.grid(row=3,column=0,padx=2,pady=10,sticky=S)

root.mainloop()
