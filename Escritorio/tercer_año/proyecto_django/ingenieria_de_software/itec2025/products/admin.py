from django.contrib import admin

# Register your models here.
from products.models import Customer, Order, OrderDetail, Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name','price','stock')
    list_filter =('name',)
    search_field = ('name', 'stock')

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')
    search_fields = ('name',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'date')
    search_fields = ('name',)



@admin.register(OrderDetail)
class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'product', 'quantity')
    search_fields = ('product__name',)