# E-Commerce Django Project

A minimal, barebones Django e-commerce app for college project.

## Features

- Product listing with category filtering
- Product detail pages
- Session-based shopping cart
- Checkout (no payment integration)
- User registration/login/logout
- Admin panel for managing products and orders

## Setup Instructions

### 1. Create and activate virtual environment (recommended)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run migrations

```bash
python manage.py migrate
```

### 4. Create superuser (for admin access)

```bash
python manage.py createsuperuser
```

### 5. Run the development server

```bash
python manage.py runserver
```

## Access Points

- **Shop**: http://127.0.0.1:8000/
- **Admin**: http://127.0.0.1:8000/admin/

## Project Structure

```
ecom/
├── manage.py
├── requirements.txt
├── README.md
├── ecom/                   # Project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── shop/                   # Main app
    ├── models.py           # Category, Product, Order, OrderItem
    ├── views.py            # All views
    ├── urls.py             # URL routing
    ├── forms.py            # CheckoutForm, RegisterForm
    ├── admin.py            # Admin configuration
    ├── cart.py             # Cart helper class
    ├── context_processors.py
    ├── tests.py            # Basic tests
    └── templates/shop/     # HTML templates
```

## Adding Sample Data

1. Go to admin panel: http://127.0.0.1:8000/admin/
2. Login with superuser credentials
3. Add categories (e.g., "Electronics", "Books", "Clothing")
4. Add products under each category

## Running Tests

```bash
python manage.py test shop
```

## Technologies Used

- Django 4.2+
- SQLite (default database)
- Bootstrap 5 (CDN)
- Session-based cart storage
