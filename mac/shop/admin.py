from django.contrib import admin

# Register your models here.
from .models import Product
admin.site.register(Product) # register product in admin panel

from .models import Contact
admin.site.register(Contact)

from .models import Orders
admin.site.register(Orders)

from .models import OrderUpdate
admin.site.register(OrderUpdate)