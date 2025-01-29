from django.shortcuts import render, redirect, get_object_or_404
from .models import product,category
from django.contrib import messages

def homepage(request):
    products = product.objects.all()
    return render(request,'homepage.html', {'products': products})

def productpage(request,product_id):
    myproduct = get_object_or_404(product, id= product_id)

    if request.method == "POST":
        return redirect('cart:cart_add',product_id=myproduct.name)

    return render(request,'product.html', {'product': myproduct})

def categorypage(request,x):
    x = x.replace('-', ' ')
    try:
        Category = category.objects.get(name=x)
        products = product.objects.filter(category = Category)
        return render(request, 'category.html', {'products': products, 'category':Category})
    except:
        messages.success(request, ("دسته بندی مورد نظر موجود نمیباشد"))
        return redirect('homepage')
    
def aboutus(request):
    return render(request,'about.html')