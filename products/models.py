from datetime import date
from django.db import models
from django.utils import timezone
# Create your models here.


class Product(models.Model):
    ProductID = models.CharField(max_length=255)
    Title = models.CharField(max_length=255)
    Rating = models.IntegerField()
    Price = models.IntegerField()
    DateAdded = models.DateField(auto_now_add=True, blank=True)
    ImageURL = models.TextField(blank=True, null=True)
    Description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.Title}"
