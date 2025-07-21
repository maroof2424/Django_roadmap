### ✅ **Day 1: Django Setup, Project Structure, and Basics**

#### 🎯 Goal:

Set up your Django environment, understand the folder structure, and run your first project.

---

### 🔧 Step 1: Install Django & Setup Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install django
```

> ✅ Tip: Name your project something like `myshop`, `myapi`, or `core`.

---

### 🛠️ Step 2: Create Django Project

```bash
django-admin startproject phase1 .
```

Project structure should look like:

```
/core
    └── core/
         ├── settings.py
         ├── urls.py
         ├── wsgi.py
         └── asgi.py
    ├── manage.py
    ├── venv/
```

---

### 🔧 Step 3: Run the Development Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` to verify Django is working ✅

---

### 🧩 Step 4: Create First App

```bash
python manage.py startapp pages
```

Add `'pages'` to `INSTALLED_APPS` in `settings.py`

---

### 📄 Step 5: Basic Home Page View

**pages/views.py**

```python
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to Django!")
```

**phase1/urls.py**

```python
from django.contrib import admin
from django.urls import path
from pages.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
]
```

---

### 📁 Step 6: Organize with Templates

Create folders:
`pages/templates/pages/home.html`

```html
<!-- home.html -->
<!DOCTYPE html>
<html>
<head><title>Django Home</title></head>
<body>
    <h1>Hello, Django!</h1>
</body>
</html>
```

Then in `views.py`:

```python
from django.shortcuts import render

def home(request):
    return render(request, 'pages/home.html')
```

---

### 🧪 Step 7: Practice Task

* Create another app named `about`
* Add `/about/` route with HTML view (template)
* Include `about` page in `urls.py`

---

### ✅ Today You Learned

* How to create a Django project
* Basic views, URLs, and templates
* How to structure your project

