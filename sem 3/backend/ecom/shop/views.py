"""
Views for the shop app.
Product listing, detail, cart, checkout, and auth.
"""
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.http import require_POST

from .models import Category, Product, Order, OrderItem
from .forms import CheckoutForm, RegisterForm
from .cart import Cart


# ============== Product Views ==============

def product_list(request, category_slug=None):
    """List all products, optionally filtered by category."""
    categories = Category.objects.all()
    products = Product.objects.all()
    current_category = None

    if category_slug:
        current_category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=current_category)

    return render(request, 'shop/product_list.html', {
        'categories': categories,
        'products': products,
        'current_category': current_category,
    })


def product_detail(request, slug):
    """Show product details."""
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'shop/product_detail.html', {
        'product': product,
    })


# ============== Cart Views ==============

def cart_detail(request):
    """Show cart contents."""
    cart = Cart(request)
    return render(request, 'shop/cart.html', {
        'cart': cart,
    })


@require_POST
def cart_add(request, product_id):
    """Add product to cart."""
    product = get_object_or_404(Product, id=product_id)
    cart = Cart(request)
    quantity = int(request.POST.get('quantity', 1))
    cart.add(product, quantity)
    messages.success(request, f'Added {product.name} to cart.')
    return redirect('shop:cart_detail')


@require_POST
def cart_update(request, product_id):
    """Update product quantity in cart."""
    cart = Cart(request)
    quantity = int(request.POST.get('quantity', 1))
    cart.update(product_id, quantity)
    messages.success(request, 'Cart updated.')
    return redirect('shop:cart_detail')


@require_POST
def cart_remove(request, product_id):
    """Remove product from cart."""
    cart = Cart(request)
    cart.remove(product_id)
    messages.success(request, 'Item removed from cart.')
    return redirect('shop:cart_detail')


# ============== Checkout Views ==============

def checkout(request):
    """Checkout page - create order from cart."""
    cart = Cart(request)

    # Don't allow checkout with empty cart
    if len(cart) == 0:
        messages.warning(request, 'Your cart is empty.')
        return redirect('shop:product_list')

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            # Create order
            order = form.save(commit=False)
            order.total = cart.get_total()
            if request.user.is_authenticated:
                order.user = request.user
            order.save()

            # Create order items
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )

            # Clear the cart
            cart.clear()
            messages.success(request, f'Order #{order.id} placed successfully!')
            return redirect('shop:checkout_complete', order_id=order.id)
    else:
        # Pre-fill form for logged-in users
        initial = {}
        if request.user.is_authenticated:
            initial['email'] = request.user.email
        form = CheckoutForm(initial=initial)

    return render(request, 'shop/checkout.html', {
        'form': form,
        'cart': cart,
    })


def checkout_complete(request, order_id):
    """Order confirmation page."""
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'shop/checkout_complete.html', {
        'order': order,
    })


# ============== Auth Views ==============

def register(request):
    """User registration."""
    if request.user.is_authenticated:
        return redirect('shop:product_list')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('shop:product_list')
    else:
        form = RegisterForm()

    return render(request, 'shop/register.html', {
        'form': form,
    })
