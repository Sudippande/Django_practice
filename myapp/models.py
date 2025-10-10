from django.db import models

# Create your models here.
class Table(models.Model):
    name=models.CharField()
    age=models.IntegerField()
    email= models.EmailField()
    address=models.CharField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    video = models.FileField(upload_to='videos/', null=True, blank=True)

    def __str__(self):
        return self.name

