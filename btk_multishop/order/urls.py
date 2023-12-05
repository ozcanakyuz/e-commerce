from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="index"),
    path("shopcart", views.shopcart, name="shopcart"),
    path("favorits", views.favorits, name="favorits"),
    path("addtocart/<int:id>", views.addtocart, name="addtocart"),
    path("addtocartfromfavorites/<int:id>", views.addtocartfromfavorites, name="addtocartfromfavorites"),
    path("addtofavorits/<int:id>", views.addtofavorits, name="addtofavorits"),
    path('deletefromcart/<int:id>', views.deletefromcart, name='deletefromcart'),
    path('deletefromfavorits/<int:id>', views.deletefromfavorits, name='deletefromfavorits'),
    path('orderproduct/', views.orderproduct, name='orderproduct'),

]