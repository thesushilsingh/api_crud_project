from django.db import models

# Create your models here.

class Product(models.Model):
    Product_Name = models.CharField(max_length=255)
    Category = models.CharField(max_length=255)
    Status = models.CharField(max_length=255)
    Amount = models.PositiveIntegerField()
    
    def __str__(self):
        return self.Product_Name