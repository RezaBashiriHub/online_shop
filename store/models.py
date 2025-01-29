from django.db import models
import datetime

class category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class product(models.Model):
    name = models.CharField(max_length=225)
    price = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(category, on_delete=models.CASCADE, default=1)
    image = models.ImageField(upload_to='uploads/product/', null=True)

    def __str__(self):
        return self.name
