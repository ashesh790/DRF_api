from django.db import models

# Create your models here.

class Student(models.Model): 
    name = models.CharField(max_length = 100, null= False) 
    age = models.IntegerField(default = 18, null= False) 
    father_name = models.CharField(max_length = 100, null= False) 

class Category(models.Model):
    category_name = models.CharField(max_length = 100) 

class Book(models.Model): 
    category= models.ForeignKey(Category, on_delete = models.CASCADE) 
    book_title = models.CharField(max_length = 100)