from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Cart(models.Model):
    product = models.CharField(max_length=225)
    quantity = models.PositiveIntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.quantity} x {self.product}'

    def get_abs_url(self):
        return reverse("cart:cart_sum")