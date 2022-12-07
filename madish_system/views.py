import json
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import FoodMenu, UserOrder, Category, ExtraFood
from .forms import FoodMenuForm, CategoryForm

# Create your views here.
def main_page(request):
    return render(request, 'main_page.html')

@login_required(login_url='login')
def administrator_panel(request):
    if request.user.is_superadmin:
        return render(request, 'administrator.html')
    else:
        return redirect('main_page')

@login_required(login_url='login')
def place_order(request):
    menus = FoodMenu.objects.all()
    extra_food_list = ExtraFood.objects.all()

    context = {
        'menus': menus,
        'extra_food_list': extra_food_list,
    }
    return render(request, 'place_order.html', context)

@login_required(login_url='login')
def order_history(request):
    orders = UserOrder.objects.filter(ordering_user=request.user).order_by('-id')
    context = {
        'orders': orders
    }
    return render(request, 'order_history.html', context)

def order_traffic(request):
    orders = UserOrder.objects.filter(delivered=False)
    context = {
        'orders': orders,
    }
    return render(request, 'order_traffic.html', context)

@login_required(login_url='login')
def order_ready(request):
    if request.user.is_superadmin:
        orders = UserOrder.objects.filter(delivered=False)
        context = {
            'orders': orders
        }
        return render(request, 'order_ready.html', context)
    else:
        return redirect('main_page')

@login_required(login_url='login')
def make_ready(request, order_id):
    if request.user.is_superadmin:
        order = UserOrder.objects.get(id=order_id)
        order.ready = True
        order.save()
        messages.success(request, 'This order is ready!')
        return redirect('order_ready')
    else:
        return redirect('main_page')

@login_required(login_url='login')
def make_delivered(request, order_id):
    if request.user.is_superadmin:
        order = UserOrder.objects.get(id=order_id)
        if not order.ready:
            messages.error(request, 'Make this order ready first!')
            return redirect('order_ready')
        else:
            order.delivered = True
            order.save()
            messages.success(request, 'This order is delivered!')
            return redirect('order_ready')
    else:
        return redirect('main_page')

@login_required(login_url='login')
def cancel_order(request, order_id):
    if request.user.is_superadmin:
        order = UserOrder.objects.get(id=order_id)
        order.delete()
        return redirect('order_ready')
    else:
        return redirect('main_page')
    
@login_required(login_url='login')
def create_category(request):
    if request.user.is_superadmin:
        if request.method == 'POST':
            form = CategoryForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'You have successfully created a new category')
                return redirect('create_category')
            else:
                messages.error(request, 'This category already exists!')
        else:
            form = CategoryForm
        context = {
            'form': form
        }
        return render(request, 'create_category.html', context)
    else:
        return redirect('main_page')

@login_required(login_url='login')
def view_category(request):
    if request.user.is_superadmin:
        view_categories = Category.objects.all()
        context = {
            'view_categories': view_categories
        }
        return render(request, 'view_category.html', context)
    else:
        return redirect('main_page')

@login_required(login_url='login')
def delete_category(request, category_id):
    if request.user.is_superadmin:
        category = Category.objects.get(id=category_id)
        category.delete()
        messages.success(request, 'You have successfully deleted the category!')
        return redirect('view_category')
    else:
        return render('main_page')

@login_required(login_url='login')
def create_menu(request):
    if request.user.is_superadmin:
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
    else:
        return redirect('main_page')

@login_required(login_url='login')
def view_menu(request):
    food_menus = FoodMenu.objects.all()
    context = {
        'food_menus': food_menus,
    }
    return render(request, 'view_menu.html', context)

@login_required(login_url='login')
def delete_menu(request, menu_id):
    if request.user.is_superadmin:
        menu = FoodMenu.objects.get(id=menu_id)
        menu.delete()
        return redirect('view_menu')
    else:
        return redirect('main_page')

@login_required(login_url='login')
def order(request):
    order_items = {
        'items': [],
        'quantities': [],
        'extra_food_collection': [],
    }
    if request.method == 'POST':
        items = request.POST.getlist('items')
        quantities = request.POST.getlist('quantities')
        comment_box = request.POST['comment_box']
        extra_food_collection = request.POST.getlist('extra_food_collection')

        if not items:
            messages.error(request, 'Please order something first!')
            return redirect('place_order') 
        
        for item in items:
            menu_item = FoodMenu.objects.get(id=int(item))
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

        if extra_food_collection:
            for extra_food in extra_food_collection:
                extra_data = {
                    'extra_food' : extra_food
                }
                order_items['extra_food_collection'].append(extra_data)

        joined_list = [dict(a, **b) for a, b in zip(order_items['items'], order_items['quantities'])]

        price = 0
        quantity = 0
        item_ids = []
        quantity_list = []

        for item in joined_list:
            price += item['price'] * int(item['quantity'])
            quantity += int(item['quantity'])
            item_ids.append(item['id'])
            quantity_list.append(item['quantity'])

        request.session['item_ids'] = item_ids
        request.session['quantity_list'] = quantity_list
        request.session['extra_food_collection'] = extra_food_collection

    context = {
        'items': order_items['items'],
        'price': price,
        'comment_box': comment_box,
        'extra_food_collection': extra_food_collection,
        'quantity_list': quantity_list,
    }

    return render(request, 'order_summary.html', context)

@login_required(login_url='login')
def confirm_order(request):
    if request.method == 'POST':
        item_ids = request.session.get('item_ids')
        quantity_list = request.session.get('quantity_list')
        extra_food_collection = request.session.get('extra_food_collection')
        price = request.POST['price']
        user_comment = request.POST['comment_box']

        order = UserOrder.objects.create(price=price, ordering_user=request.user, user_comment=user_comment)
        order.set_quantity(quantity_list)
        order.set_extra_food(extra_food_collection)
        order.food_menu.add(*item_ids)
        order.save()
        messages.success(request, 'You have successfully created an order!')
        return redirect('order_traffic')
    else:
        return redirect('place_order')

@login_required(login_url='login')
def record(request):
    if request.user.is_superadmin:
        orders = UserOrder.objects.filter(delivered=True).order_by('-id')
        context = {
            'orders': orders,
        }
        return render(request, 'record.html', context)
    else:
        return redirect('main_page')


def contact_us(request):
    return render(request, 'contact_us.html')