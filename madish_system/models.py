import json
from django.db import models
from django.core.validators import MinValueValidator
from accounts.models import Account

# My models

class FoodMenu(models.Model):
    name = models.CharField('Name', max_length=120, unique=True)
    image = models.ImageField('Images', upload_to='photos/menus_image')
    detail = models.TextField('Detail', max_length=255, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.ManyToManyField('Category', related_name='item')
    with_extra = models.BooleanField('With Extra', default=False)
    
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class ExtraFood(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'extra food'
        verbose_name_plural = 'extra food'

    def __str__(self):
        return self.name

class UserOrder(models.Model):
    ordering_user = models.ForeignKey(Account, on_delete=models.CASCADE)
    food_menu = models.ManyToManyField('FoodMenu', related_name='order')
    price = models.DecimalField(max_digits=7, decimal_places=2)
    quantity = models.CharField('Quantity', max_length=255)
    ready = models.BooleanField('Ready', default=False)
    delivered = models.BooleanField('Delivered', default=False)
    user_comment = models.TextField('User Comment', max_length=255, blank=True)
    extra_food = models.CharField('Extra Food', max_length=255, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ordering_user.first_name

    def set_extra_food(self, lst):
        self.extra_food = json.dumps(lst)

    def set_quantity(self, lst):
        self.quantity = json.dumps(lst)
    
    def get_extra_food(self):
        return json.loads(self.extra_food)

    def get_quantity(self):
        return json.loads(self.quantity)