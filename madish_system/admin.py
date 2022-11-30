from django.contrib import admin
from .models import FoodMenu, UserOrder, Size, Extra
# Register your models here

@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ('size',)
    search_fields = ('size',)

@admin.register(Extra)
class ExtraAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name',)

@admin.register(FoodMenu)
class FoodMenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'has_size')
    search_fields = ('name',)

@admin.register(UserOrder)
class UserOrderAdmin(admin.ModelAdmin):
    list_display = ('ordering_user', 'size', 'extra', 'quantity')
    search_fields = ('ordering_user', 'food_menu')

