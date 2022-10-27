from django.db import models

# Create your models here.

class Post(models.Model):
    email = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.email