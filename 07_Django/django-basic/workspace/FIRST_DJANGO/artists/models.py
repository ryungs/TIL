from django.db import models

# Create your models here.
class Band(models.Model):
    name = models.CharField(max_length=50)
    debut = models.IntegerField()
    is_active = models.BooleanField(default=True)
    description = models.TextField(default='No descriptions yet..')
    
def __str__(self):
    return f'{self.id}: {self.name}'
