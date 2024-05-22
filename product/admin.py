from django.contrib import admin
from .models import CategoryFood,Foods,Cart,CartItem
# Register your models here.

admin.site.register(CategoryFood)
admin.site.register(Foods)
admin.site.register(Cart)
admin.site.register(CartItem)