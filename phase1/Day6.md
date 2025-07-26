## 🛒 **Day 6: Task – Mini MyShop with Admin Panel**

### ✅ Objective:

Build a small functional eCommerce backend (admin panel) with:

* Categories
* Products
* Images
* Admin management

---

### ✅ Models Recap:

You should already have:

```python
# models.py
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
```

---

### ✅ Admin Panel Setup:

```python
# admin.py
from django.contrib import admin
from .models import Product, Category

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
```

---

### ✅ Project Folder Structure

```
myshop/
│
├── myshop/           # settings.py, urls.py
├── shop/             # your app
│   ├── models.py
│   ├── admin.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
│       └── shop/
│           ├── base.html
│           ├── home.html
│           ├── product_list.html
│           └── product_detail.html
├── static/
│   └── style.css
└── media/
    └── products/
```

---

### ✅ Steps to Build

1. **Run Migrations**

```bash
python manage.py makemigrations
python manage.py migrate
```

2. **Create Admin Superuser**

```bash
python manage.py createsuperuser
```

3. **Run the Server**

```bash
python manage.py runserver
```

4. **Login to Admin Panel**
   Visit [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

5. **Add Categories and Products** via Admin Panel

---

### ✅ Optional: Build a Product Listing Page

In `views.py`:

```python
from django.shortcuts import render
from .models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop/product_list.html', {'products': products})
```

In `urls.py`:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
]
```

In `templates/shop/product_list.html`:

```html
{% extends 'shop/base.html' %}
{% block content %}
<h2>Products</h2>
<div class="row">
    {% for product in products %}
        <div class="col-md-4">
            <div class="card mb-3">
                <img src="{{ product.image.url }}" class="card-img-top">
                <div class="card-body">
                    <h5 class="card-title">{{ product.name }}</h5>
                    <p class="card-text">PKR {{ product.price }}</p>
                </div>
            </div>
        </div>
    {% endfor %}
</div>
{% endblock %}
```

---

### ✅ Checklist for Day 6

* [x] Models for Product & Category
* [x] Admin panel with customization
* [x] Add sample data via admin
* [ ] Optional: Frontend to list products
* [ ] Media images properly loading (use `MEDIA_URL`, `MEDIA_ROOT`)
* [ ] Custom CSS for styles

---
