from django.contrib import admin

from order.models import Favorites, ShopCart, OrderProduct, Order


# Register your models here.
class ShopCartAdmin(admin.ModelAdmin):
    list_display = ['product','user','quantity','price','amount' ]
    list_filter = ['user']
admin.site.register(ShopCart,ShopCartAdmin)

class FavoriteCartAdmin(admin.ModelAdmin):
    list_display = ['product','user','quantity','price','amount' ]
    list_filter = ['user']
admin.site.register(Favorites, FavoriteCartAdmin)


class OrderProductline(admin.TabularInline):
    model = OrderProduct
    readonly_fields = ('user','product','price','quantity','amount')
    can_delete = False
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name','phone','city','total','status']
    list_filter = ['status']
    readonly_fields = ('user','address','city','country','first_name','ip', 'last_name','phone','city','total')
    can_delete = False
    inlines = [OrderProductline]
admin.site.register(Order,OrderAdmin)


class OrderProductAdmin(admin.ModelAdmin):
    list_display = ['user', 'product','price','quantity','amount']
    list_filter = ['user']
admin.site.register(OrderProduct,OrderProductAdmin)

