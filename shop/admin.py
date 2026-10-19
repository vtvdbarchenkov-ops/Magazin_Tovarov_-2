# Register your models here.
from django.contrib import admin
from shop.models import *

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')
    list_filter = ('category',)
    search_fields = ('name', 'description')
    list_editable = ('price',)

@admin.register(Warranty)
class WarrantyAdmin(admin.ModelAdmin):
    list_display = ('product', 'date', 'service_center')
    list_filter = ('date',)
    search_fields = ('service_center', 'product__name')

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'name', 'email', 'phone')
    list_filter = ('last_name',)
    search_fields = ('name', 'last_name', 'email', 'phone')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer')
    list_filter = ('customer',)
    search_fields = ('customer__name', 'customer__last_name')