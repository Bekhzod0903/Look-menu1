from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

class CategoryFood(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'category_food'

    def __str__(self):
        return self.name

class Foods(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    category = models.ForeignKey(CategoryFood, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='foods_image/', blank=True, null=True, default='default_img/food_img.png')

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        db_table = 'foods'

    def __str__(self):
        return self.name

from django.db import models
from django.conf import settings

class Cart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart({self.user.username})"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    food = models.ForeignKey(Foods, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.food.name}"
