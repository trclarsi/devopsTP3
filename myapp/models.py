from django.db import models

class MyModel(models.Model): name = models.CharField(max_length=150)
# Create your models here.
def __str__(self): return self.name