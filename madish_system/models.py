from django.db import models
from django.core.validators import MinValueValidator
from accounts.models import Account

# My models
class Size(models.Model):
    size = models.DecimalField('Size', max_digits=5,decimal_places=2)

    def __str__(self):
        return str(self.size)

class Extra(models.Model):
    name = models.CharField('Name', max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name

class FoodMenu(models.Model):
    name = models.CharField('Name', max_length=120, unique=True)
    image = models.ImageField('Images', upload_to='photos/menus_image')
    detail = models.TextField('Detail', max_length=255, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    has_size = models.BooleanField('Has Size', default=True)
    
    def __str__(self):
        return self.name

class UserOrder(models.Model):
    ordering_user = models.ForeignKey(Account, on_delete=models.CASCADE)
    food_menu = models.ManyToManyField('FoodMenu', related_name='order')
    price = models.DecimalField(max_digits=7, decimal_places=2)
    size = models.ForeignKey(Size, on_delete=models.CASCADE, blank=True, null=True)
    extra = models.ForeignKey(Extra, on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)], default=1)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ordering_user.first_name
    