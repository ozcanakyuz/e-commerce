from django.urls import include, path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("shop", views.shop, name="shop"),
    path("detail", views.detail, name="detail"),
    path("contact", views.contact, name="contact"),
    path("checkout", views.checkout, name="checkout"),
    path('login', views.login_view, name='login_view'),
    path('signup', views.signup_view, name='signup_view'),
    path('logout',views.logout_view, name= 'logout_view'),



]