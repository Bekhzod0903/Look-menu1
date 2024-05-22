from django.urls import path
from .views import FoodListView, FoodDetailView, view_cart, add_to_cart

app_name = 'product'
urlpatterns = [
    path('test/', FoodListView.as_view(), name='food-list'),
    path('detail/<int:pk>/', FoodDetailView.as_view(), name='food-detail'),
    path('add-to-cart/<int:food_id>/', add_to_cart, name='add-to-cart'),
    path('cart/', view_cart, name='view-cart'),
]
