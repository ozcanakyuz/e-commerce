from django.http import HttpResponse
from django.shortcuts import render

from order.models import ShopCart

def index(request):
    return HttpResponse("order")

def shopcart(request):
    current_user = request.user  # Access User Session information
    shopcart = ShopCart.objects.filter(user_id=current_user.id)
    total=0
    for rs in shopcart:
        total += rs.product.price * rs.quantity
        print(total)

    context={'shopcart': shopcart,
             'total': total,
             }
    return render(request,'shopcart_products.html',context)