from django.db import models


class Student(models.Model):
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=277)
   
    
    
    def __str__(self):
        return str(self.name)