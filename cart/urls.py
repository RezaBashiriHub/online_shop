from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_sum, name='cart_sum'),
    path('add/<str:product_id>', views.cart_add, name='cart_add'),
    path('delete/<int:cart_item_id>', views.cart_del, name='cart_del'),
]
