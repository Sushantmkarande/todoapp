from django.db import models

# Create your models here.
class todoitem(models.Model):
    text = models.TextField()