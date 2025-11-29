"""
Cart utilities - session-based shopping cart.
"""
from decimal import Decimal
from .models import Product


class Cart:
    """
    Session-based shopping cart.
    Stores cart as: { product_id: { 'quantity': n, 'price': 'decimal_string' } }
    """

    def __init__(self, request):
        """Initialize cart from session."""
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}
        self.cart = cart

    def save(self):
        """Mark session as modified to save changes."""
        self.session.modified = True

    def add(self, product, quantity=1):
        """Add product to cart or update quantity."""
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {
                'quantity': 0,
                'price': str(product.price)
            }
        self.cart[product_id]['quantity'] += quantity
        self.save()

    def update(self, product_id, quantity):
        """Update quantity for a product."""
        product_id = str(product_id)
        if product_id in self.cart:
            if quantity > 0:
                self.cart[product_id]['quantity'] = quantity
            else:
                self.remove(product_id)
            self.save()

    def remove(self, product_id):
        """Remove product from cart."""
        product_id = str(product_id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def clear(self):
        """Clear the cart."""
        del self.session['cart']
        self.save()

    def __iter__(self):
        """Iterate over cart items, fetching product objects."""
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()

        for product in products:
            cart[str(product.id)]['product'] = product

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        """Return total number of items in cart."""
        return sum(item['quantity'] for item in self.cart.values())

    def get_total(self):
        """Return total price of cart."""
        return sum(
            Decimal(item['price']) * item['quantity']
            for item in self.cart.values()
        )
