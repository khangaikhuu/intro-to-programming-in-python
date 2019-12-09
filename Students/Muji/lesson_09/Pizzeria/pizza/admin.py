from django.contrib import admin
from .models import Pizzas, Topping
# Register your models here.

admin.site.register(Pizzas)
admin.site.register(Topping)
