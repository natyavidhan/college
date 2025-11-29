"""
Context processor for cart item count.
"""
from .cart import Cart


def cart_counter(request):
    """Add cart item count to template context."""
    cart = Cart(request)
    return {'cart_count': len(cart)}
