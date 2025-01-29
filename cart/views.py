from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Cart
from store.models import product
from .models import User

@login_required #ok
def cart_add(request, product_id):
    cart_item = Cart.objects.filter(user=request.user, product=product_id).first()


    if cart_item:
        cart_item.quantity += 1
        cart_item.save()
        messages.success(request, ("محصول به سبدتان اضافه شد"))
    
    else :
        Cart.objects.create(user= request.user, product= product_id)
        messages.success(request, ("محصول به سبدتان اضافه شد"))

    return redirect('cart:cart_sum')


@login_required
def cart_del(request, cart_item_id):
    cart_item = get_object_or_404(Cart, id= cart_item_id)

    if cart_item.user == request.user:
        cart_item.delete()
        messages.success(request, ("محصول از سبد حذف شد"))

    return redirect("cart:cart_sum")


@login_required
def cart_sum(request):
    cart_items = Cart.objects.filter(user = request.user)
    myfirst = request.user.first_name
    mylast = request.user.last_name
    mycategory = product.category.get_queryset()
    myprice = product.objects.values_list('price')
    

    context = {
        "cart_items": cart_items,
        "myfirst": myfirst,
        "mylast": mylast,
        "mycategory": mycategory,
        "myprice": myprice,
    }
    return render(request, "cart/cart_sum.html",context)