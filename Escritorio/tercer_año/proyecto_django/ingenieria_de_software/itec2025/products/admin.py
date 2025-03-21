from django.contrib import admin

from .models import product
# Register your models here.
@admin.register(product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name','price')
    list_filter = ['name',]#filtro
    search_fields = ('name','stock')#buscador