from django.views.generic import ListView, DetailView
from .models import Foods
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .models import Cart, CartItem, Foods


class FoodListView(ListView):
    model = Foods
    template_name = 'food/food_list.html'
    context_object_name = 'food'
    ordering = ['name']

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Foods.objects.filter(name__icontains=query)
        return super().get_queryset()

class FoodDetailView(DetailView):
    model = Foods
    template_name = 'food/food_detail.html'
    context_object_name = 'food'




def add_to_cart(request, food_id):
    food = get_object_or_404(Foods, id=food_id)
    cart, created = Cart.objects.get_or_create(user=request.user)

    cart_item, created = CartItem.objects.get_or_create(cart=cart, food=food)
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('product:food-list')

def view_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    return render(request, 'product/cart.html', {'cart': cart})









