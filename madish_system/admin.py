from django.contrib import admin
from .models import FoodMenu, UserOrder, Category, ExtraFood
# Register your models here

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(ExtraFood)
class ExtraFoodAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(FoodMenu)
class FoodMenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'price',)
    search_fields = ('name',)

@admin.register(UserOrder)
class UserOrderAdmin(admin.ModelAdmin):
    list_display = ('ordering_user', 'quantity', 'ready', 'delivered')
    search_fields = ('ordering_user', 'food_menu')

