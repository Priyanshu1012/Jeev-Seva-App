from django.db import models

# Create your models here.
class Register(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=30)
    contact_no = models.IntegerField()
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    address = models.CharField(max_length=200)

class Animaldisease(models.Model):
    type = models.CharField(max_length=50)
    disease = models.CharField(max_length=50)
    priority = models.CharField(max_length=50)
    image = models.ImageField(upload_to='')
    description = models.CharField(max_length=200)







