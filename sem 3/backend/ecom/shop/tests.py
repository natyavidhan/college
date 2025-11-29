"""
Tests for the shop app.
"""
from decimal import Decimal
from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Category, Product, Order, OrderItem


class ProductModelTest(TestCase):
    """Test Product model."""

    def setUp(self):
        self.category = Category.objects.create(name='Electronics', slug='electronics')
        self.product = Product.objects.create(
            category=self.category,
            name='Test Product',
            slug='test-product',
            description='A test product',
            price=Decimal('99.99'),
            inventory=10
        )

    def test_product_str(self):
        """Test product string representation."""
        self.assertEqual(str(self.product), 'Test Product')


class CartTest(TestCase):
    """Test cart functionality."""

    def setUp(self):
        self.client = Client()
        self.category = Category.objects.create(name='Books', slug='books')
        self.product = Product.objects.create(
            category=self.category,
            name='Django Book',
            slug='django-book',
            price=Decimal('29.99'),
            inventory=5
        )

    def test_add_to_cart(self):
        """Test adding product to cart."""
        response = self.client.post(
            f'/cart/add/{self.product.id}/',
            {'quantity': 2}
        )
        # Should redirect to cart
        self.assertEqual(response.status_code, 302)
        # Check session has cart
        session = self.client.session
        self.assertIn('cart', session)
        self.assertIn(str(self.product.id), session['cart'])
        self.assertEqual(session['cart'][str(self.product.id)]['quantity'], 2)


class CheckoutTest(TestCase):
    """Test checkout functionality."""

    def setUp(self):
        self.client = Client()
        self.category = Category.objects.create(name='Clothing', slug='clothing')
        self.product = Product.objects.create(
            category=self.category,
            name='T-Shirt',
            slug='t-shirt',
            price=Decimal('19.99'),
            inventory=10
        )
        # Add item to cart first
        self.client.post(f'/cart/add/{self.product.id}/', {'quantity': 1})

    def test_checkout_creates_order(self):
        """Test that checkout creates an order."""
        response = self.client.post('/checkout/', {
            'full_name': 'John Doe',
            'address': '123 Main St',
            'email': 'john@example.com'
        })
        # Should redirect to order complete page
        self.assertEqual(response.status_code, 302)
        # Check order was created
        self.assertEqual(Order.objects.count(), 1)
        order = Order.objects.first()
        self.assertEqual(order.full_name, 'John Doe')
        self.assertEqual(order.total, Decimal('19.99'))
        # Check order item was created
        self.assertEqual(order.items.count(), 1)
        self.assertEqual(order.items.first().product, self.product)
