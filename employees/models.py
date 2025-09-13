from django.db import models

# Create your models here.

class Employee(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    email=models.EmailField(unique=True,max_length=254)
    phone=models.CharField(max_length=15, blank=True) # blank=True means this field is optional
    photo=models.ImageField(upload_to='images')
    created_at=models.DateTimeField(auto_now_add=True) # auto_now_add=True means this field will be set to now when the object is first created.
    updated_at=models.DateTimeField(auto_now=True) # auto_now=True means this field will be set to now every time the object is saved.

    def __str__(self):
        return self.first_name


    
