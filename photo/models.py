from django.db import models

class Photo(models.Model):
    name = models.CharField(max_length=255)
    filetype = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name