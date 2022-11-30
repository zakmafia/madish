from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('administrator_panel/', views.administrator_panel, name='administrator_panel'),
    path('place_order/', views.place_order, name='place_order'),
    path('order_history/', views.order_history, name='order_history'),
    path('order_traffic/', views.order_traffic, name='order_traffic'),
    path('create_menu/', views.create_menu, name='create_menu'),
    path('view_menu/', views.view_menu, name='view_menu'),
    path('view_extra_menu/', views.view_extra_food, name='view_extra_food'),
    path('delete_menu/<menu_id>/', views.delete_menu, name='delete_menu'),
    path('extra_food/', views.extra_food, name='extra_food'),
    path('delete_extra_food/<extra_id>/', views.delete_extra_food, name='delete_extra_food'),
    path('manage_size/', views.manage_size, name='manage_size'),
    path('view_available_size/', views.view_available_size, name='view_available_size'),
    path('delete_size/<size_id>/', views.delete_size, name='delete_size'),
    path('order', views.order, name='order')
]
