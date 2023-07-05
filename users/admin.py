from django.contrib import admin
from products.models import Product
from users.models import Cart, Orders

# from users.models import User

# Register your models here.
admin.site.register(Cart)
admin.site.register(Orders)
