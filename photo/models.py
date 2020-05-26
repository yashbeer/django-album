from django.db import models
from django.contrib.auth import get_user_model

class Photo(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, default=0)
    name = models.CharField(max_length=255, db_index=True)
    filetype = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name