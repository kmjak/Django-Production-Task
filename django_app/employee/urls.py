from django.urls import path
from . import views

urlpatterns = [
    path('login',views.login,name="login"),
    path('logout',views.logout,name="logout"),
    path('home',views.home,name='home'),
    path('order_management/', views.home, name='order_management'),
    path('customer_management/', views.customers_list, name='customer_management'),
    path('customer_management/<str:pk>/', views.customer_details, name='customer_management'),
    path('customer_edit/<str:pk>/', views.customer_edit, name='customer_edit'),
    path('customer_delete/<str:pk>/', views.customer_delete, name='customer_delete'),
    path('order_aggregate_by_customer/', views.home, name='order_aggregate_by_customer'),
    path('order_aggregate_management_by_product/', views.home, name='order_aggregate_management_by_product'),
    path('order_history_by_customer/', views.home, name='order_history_by_customer'),
    path('order_history_by_product/', views.home, name='order_history_by_product'),
    path('division_information/', views.home, name='division_information'),
    path('production_information/', views.home, name='production_information'),
    path('inventory_management_product/', views.home, name='inventory_management_product'),
    path('arrival_management_product/', views.home, name='arrival_management_product'),
    path('product_information/', views.home, name='product_information'),
    path('inventory_information/', views.home, name='inventory_information'),
    path('shipping_information/', views.home, name='shipping_information'),
]