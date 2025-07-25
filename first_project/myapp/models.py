from django.db import models

# Create your models here.database ko lagi model banunu parxa
class Contact(models.Model):
    name= models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    file=models.FileField(upload_to='uploads/')
    number=models.CharField(max_length=10)
    feedback=models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.name

class Signup(models.Model):
    fullname=models.CharField(max_length=120)
    address=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=20)
    conform=models.CharField(max_length=20)
    date=models.DateField()


