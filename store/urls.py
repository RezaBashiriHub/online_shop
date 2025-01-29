from django.urls import path
from .views import homepage
from . import views

urlpatterns = [
    path('', homepage, name='homepage'),
    path('product/<int:product_id>',views.productpage, name='product'),
    path('category/<str:x>', views.categorypage, name='category'),
    path('aboutus', views.aboutus, name='aboutus'),
]
