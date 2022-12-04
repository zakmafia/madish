from django.shortcuts import render, redirect
from django.contrib import messages
from .models import FoodMenu, UserOrder
from .forms import FoodMenuForm

# Create your views here.
def main_page(request):
    return render(request, 'main_page.html')

def administrator_panel(request):
    return render(request, 'administrator.html')

def place_order(request):
    menus = FoodMenu.objects.all()

    context = {
        'menus': menus,
    }
    return render(request, 'place_order.html', context)

def order_history(request):
    orders = UserOrder.objects.filter(ordering_user=request.user).order_by('-id')
    context = {
        'orders': orders
    }
    return render(request, 'order_history.html', context)

def order_traffic(request):
    orders = UserOrder.objects.all().order_by('-id')
    context = {
        'orders': orders,
    }
    return render(request, 'order_traffic.html', context)

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

def order(request):
    order_items = {
        'items': [],
        'quantities': [],
    }
    if request.method == 'POST':
        items = request.POST.getlist('items')
        quantities = request.POST.getlist('quantities')

        for item in items:
            menu_item = FoodMenu.objects.get(pk__contains=int(item))
            item_data = {
                'id': menu_item.pk,
                'name': menu_item.name,
                'price': menu_item.price,
            }

            order_items['items'].append(item_data)

        for quantity in quantities:
            quantity_data = {
                'quantity': quantity
            }
            order_items['quantities'].append(quantity_data)

        joined_list = [dict(a, **b) for a, b in zip(order_items['items'], order_items['quantities'])]
                    
        price = 0
        quantity = 0
        item_ids = []

        for item in joined_list:
            price += item['price'] * int(item['quantity'])
            quantity += int(item['quantity'])
            item_ids.append(item['id'])

        order = UserOrder.objects.create(price=price, ordering_user=request.user, quantity=quantity)
        order.food_menu.add(*item_ids)


    context = {
        'items': order_items['items'],
        'price': price
    }

    return render(request, 'order_confirmation.html', context)