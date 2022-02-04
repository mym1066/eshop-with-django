from django.contrib import admin
from eshop_order.models import OrderDetail

from eshop_order.models import Order

# Register your models here.
admin.site.register(Order)
admin.site.register(OrderDetail)