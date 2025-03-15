"""
URL configuration for stock_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from inventory.views import stock_list, update_stock, delete_stock_item, add_stock
from inventory.views import update_price 

urlpatterns = [
    path('', stock_list, name='stock_list'),
    path('update_stock/<int:pk>/', update_stock, name='update_stock'),
    path('delete/<int:item_id>/', delete_stock_item, name='delete_stock_item'),
    path('add/', add_stock, name='add_stock'),
    path('update-price/<int:item_id>/', update_price, name='update_price'),

]


