from distutils.command.upload import upload
from random import random
from unicodedata import category
from django.shortcuts import render,redirect
from PIL import ImageGrab
import win32com
import win32com.client as win32
import pythoncom
import email
import pandas as pd
from .models import Products, Filestorage
# from functools import lru_cache
# from django.contrib.staticfiles import finders
import uuid
import os.path
from django.core.files import File


def landing(request):
    print(request)
    if request.method == 'POST':
       xl=win32com.client.Dispatch("Excel.Application",pythoncom.CoInitialize())
       username='regionald@gmail.com'
       file=request.FILES.get('file')
     
       
       file_Upload=Filestorage.objects.create(
         file_Name=file,
        )
       file_Name=file_Upload.file_Name
       file_path=f'C:\\Users\\Terry\\projects\\catalog\\catalog\\static\\images\\{file_Name}'
       print(file_path)
       
       print(file)
       excel = win32.gencache.EnsureDispatch('Excel.Application')
       
       workbook = excel.Workbooks.Open(file_path)
       
       df = pd.read_excel(file_path)
       head=df.columns
       print(head)
       image_path='C:\\Users\\Terry\\projects\\catalog\\catalog\\static\\images\\'

       for sheet in workbook.Worksheets:
         for name,category,price,descript,shape in zip(df.Name,df.Category,df.Price,df.Description,sheet.Shapes):
           print(name,category,price,descript)
           pic_name=uuid.uuid1()
          
           if shape.Name.startswith('Picture'):  # or try 'Image'
                  shape.Copy()
                 #os.mkdir(save_path)
                  image = ImageGrab.grabclipboard()
                  image.save(f'{image_path}{pic_name}.PNG', 'PNG')
           try:
             user=Products.objects.create(
              username=username,
              category=category,
              name=name,
              price=price,
              descript=descript,
              avater=f'{pic_name}.PNG')
           except:
             print('Try')
                
    return render(request,'base/asset.html')
