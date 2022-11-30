from django.shortcuts import render, redirect
from django.contrib import messages
from .models import FoodMenu, UserOrder, Size, Extra
from .forms import FoodMenuForm, ExtraForm, SizeForm

# Create your views here.
def main_page(request):
    return render(request, 'main_page.html')

def administrator_panel(request):
    return render(request, 'administrator.html')

def place_order(request):
    menus = FoodMenu.objects.all()
    sizes = Size.objects.all()
    extra_foods = Extra.objects.all()
    context = {
        'menus': menus,
        'sizes': sizes,
        'extra_foods': extra_foods,
    }
    return render(request, 'place_order.html', context)

def order_history(request):
    return render(request, 'order_history.html')

def order_traffic(request):
    return render(request, 'order_traffic.html')

def create_menu(request):
    if request.method == 'POST':
        form = FoodMenuForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully created a new menu')
            return redirect('create_menu')
        else:
            messages.error(request, 'This menu already exists!')
    else:
        form = FoodMenuForm
    context = {
        'form': form
    }       
    return render(request, 'create_menu.html', context)

def view_menu(request):
    food_menus = FoodMenu.objects.all()
    context = {
        'food_menus': food_menus,
    }
    return render(request, 'view_menu.html', context)

def delete_menu(request, menu_id):
    menu = FoodMenu.objects.get(id=menu_id)
    menu.delete()
    return redirect('view_menu')

def extra_food(request):
    if request.method == 'POST':
        form = ExtraForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully created an extra food')
            return redirect('extra_food')
        else:
            messages.error(request, 'This name already exists!')
    else:
        form = ExtraForm
    context = {
        'form': form,
    }
    return render(request, 'extra_food.html', context)

def view_extra_food(request):
    extra_foods = Extra.objects.all()
    context = {
        'extra_foods': extra_foods,
    }
    return render(request, 'view_extra_food.html', context)

def delete_extra_food(request, extra_id):
    extra = Extra.objects.get(id=extra_id)
    extra.delete()
    return redirect('view_extra_food')

def manage_size(request):
    if request.method == 'POST':
        form = SizeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully created a size')
            return redirect('manage_size')
        else:
            messages.error(request, 'This size already exists!')
    else:
        form = SizeForm
    context = {
        'form': form,
    }
    return render(request, 'manage_size.html', context)

def view_available_size(request):
    sizes = Size.objects.all()
    context = {
        'sizes': sizes,
    }
    return render(request, 'view_available_size.html', context)

def delete_size(request, size_id):
    size = Size.objects.get(id=size_id)
    size.delete()
    return redirect('view_available_size')

def order(request):
    order_items = {
        'items': [],
    }
    if request.method == 'POST':
        items = request.POST.getlist('items[]')
        for item in items:
            menu_item = FoodMenu.objects.get(pk__contains=int(item))
            item_data = {
                'id': menu_item.pk,
                'name': menu_item.name,
                'price': menu_item.price
            }

            order_items['items'].append(item_data)
        
        price = 0
        item_ids = []

        for item in order_items['items']:
            price += item['price']
            item_ids.append(item['id'])

        order = UserOrder.objects.create(price=price, ordering_user=request.user)
        order.food_menu.add(*item_ids)


    context = {
        'items': order_items['items'],
        'price': price
    }

    return render(request, 'order_confirmation.html', context)