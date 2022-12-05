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
    path('create_category/', views.create_category, name='create_category'),
    path('view_category/', views.view_category, name='view_category'),
    path('delete_category/<category_id>/', views.delete_category, name='delete_category'),
    path('delete_menu/<menu_id>/', views.delete_menu, name='delete_menu'),
    path('order/', views.order, name='order'),
    path('order_ready/', views.order_ready, name='order_ready'),
    path('make_ready/<order_id>/', views.make_ready, name='make_ready'),
    path('make_delivered/<order_id>/', views.make_delivered, name='make_delivered'),
    path('record/', views.record, name='record'),

    path('contact_us/', views.contact_us, name='contact_us')
]
