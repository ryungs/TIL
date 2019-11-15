from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=80)
    birthday = models.DateField()
    age = models.IntegerField(default=20)
    
    def __str__(self):
        return f'{self.id}: {self.name}'