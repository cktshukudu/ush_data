from django.db import models

# Create your models here.
class Products(models.Model):
    username=models.CharField(max_length=45,default='No name')
    category=models.CharField(max_length=30,)
    name=models.CharField(max_length=30,)
    price=models.FloatField(default=0)
    descript=models.CharField(max_length=30,)
    avater=models.ImageField(null=True,default="images.png")

class Filestorage(models.Model):
    file_Name=models.FileField(null=True,default="images.png")   