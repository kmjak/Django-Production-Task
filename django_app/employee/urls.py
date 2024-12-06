from django.urls import path
from . import views

urlpatterns = [
    path('login',views.login,name="login"),
    path('logout',views.logout,name="logout"),
    path('home',views.home,name='home'),
    path('order_management/', views.home, name='order_management'),
    path('customer_management/', views.customers_list, name='customer_management'),
    path('customer_management/<str:pk>/', views.customer_details, name='customer_management'),
    path('product_management/', views.home, name='product_management'),
    path('stock_management/', views.home, name='stock_management'),
    path('order_aggregate/', views.home, name='order_aggregate'),
    path('employee_information/', views.home, name='employee_information'),
    path('division_information/', views.home, name='division_information'),
    path('production_information/', views.home, name='production_information'),
    path('inventory_management_product/', views.home, name='inventory_management_product'),
    path('arrival_management_product/', views.home, name='arrival_management_product'),
    path('product_information/', views.home, name='product_information'),
    path('inventory_information/', views.home, name='inventory_information'),
    path('shipping_information/', views.home, name='shipping_information'),
]