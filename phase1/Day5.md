## ✅ **Day 5 – Models, Migrations, Admin Panel**

### 📚 Topics:

* Django Models
* Migrations (`makemigrations`, `migrate`)
* Admin Panel Customization
* Relations (`ForeignKey`)
* Registering Models in Admin

---

### 🔧 Tasks:

* [x] Create `Category` model (e.g., name, slug)
* [x] Create `Product` model (e.g., name, price, image, category as ForeignKey)
* [x] Run `makemigrations` and `migrate`
* [x] Register models in `admin.py`
* [x] Customize admin list display
* [x] Upload products via admin
* [x] Show products on homepage with Bootstrap cards

---

### 🧪 Practice

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

```python
# models.py
from django.db import models

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

