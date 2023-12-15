# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 20:37:10 2023

@author: lenovo
"""

 
import io 
from tkinter import filedialog
import webbrowser
import tkinter as tk
from tkinter import *

from tkinter import ttk
import datetime
import openpyxl
from openpyxl import Workbook
from PIL import Image
import numpy as np
from skimage import transform
def load(filename):
   np_image = Image.open(filename)
   np_image = np.array(np_image).astype('float32')/255
   np_image = transform.resize(np_image, (150, 150,1))
   np_image = np.expand_dims(np_image, axis=0)
   return np_image

#############################
####fffffffffffffffffffffffffffffffffffffff



def hh():   
     
  def load(filename):
    np_image = Image.open(filename)
    np_image = np.array(np_image).astype('float32')/255
    np_image = transform.resize(np_image, (150, 150,1))
    np_image = np.expand_dims(np_image, axis=0)
    return np_image
  img=load(b9.get())
  from tensorflow.keras.models import load_model
  new_model = load_model(r'C:\Users\lenovo\Desktop\chest\chest_model.h5')

 
  pr_new=new_model.predict(img)
  if pr_new > 0.5:
      b8.delete(0,"end")
      b8.insert(0,"not normal")
   
  else:
      b8.delete(0,"end")
      b8.insert(0,"normal")
    
def select():
    der=filedialog.askopenfilename()
    b9.delete(0,"end")
    b9.insert(0,der)
      
   

b1=Button(root,text='تشخيص ',fg='white',font=('Tajawal 12'),width=15,bg='#6D8B74',bd=1,relief=SOLID,cursor='hand2',height=1,command=hh)
b1.place(x=500,y=400)

b2=Button(root,text='اختيار صوره',fg='white',font=('Tajawal 12'),width=15,bg='#6D8B74',bd=1,relief=SOLID,cursor='hand2',height=1,command=select)
b2.place(x=300,y=400)

b9=Entry(root,fg='white',font=('Tajawal 12'),width=30,bg='gray',bd=1,relief=SOLID,cursor='hand2')
b9.place(x=340,y=360)
b8=Label(root,fg='white',font=('Tajawal 12'),width=30,height=12,bg='gray',bd=1,relief=SOLID,cursor='hand2')
b8.place(x=340,y=100)
b8=Entry(root,fg='white',font=('Tajawal 12'),width=10,bd=1,bg='gray',relief=SOLID,cursor='hand2')
b8.place(x=430,y=330)
    
root.mainloop()    
    
