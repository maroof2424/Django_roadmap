## 📅 Phase 1 - Day 2: Django Homepage Setup (No REST)

### ✅ Objective

Set up a basic homepage using Django views, templates, and Bootstrap — **without Django REST Framework**.

---

### 📁 Folder Structure (After Day 2)

```
phase1/
├── manage.py
├── phase1/               # Project folder
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── home/                 # App folder
    ├── __init__.py
    ├── views.py
    ├── urls.py
    ├── templates/
    │   └── home.html
    └── static/           # (Optional for future CSS/JS)
```

---

### 🛠️ What Was Done Today

#### 1. Created Django App

```bash
python manage.py startapp home
```

#### 2. Registered App in `settings.py`

```python
INSTALLED_APPS = [
    ...
    'home',
]
```

#### 3. Setup `urls.py`

* **Project-level `phase1/urls.py`:**

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
]
```

* **App-level `home/urls.py`:**

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
```

#### 4. Created `home.html` in `home/templates/`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Phase1 - Home</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="bg-dark text-white d-flex align-items-center justify-content-center vh-100">
    <div class="text-center">
        <h1 class="display-4">Welcome to Phase1</h1>
        <p class="lead">This is your homepage using Django + Bootstrap only</p>
    </div>
</body>
</html>
```

#### 5. Setup `views.py`

```python
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
```

---

### 🎯 Output Preview

* Dark themed centered homepage with Bootstrap.
* Message: `"Welcome to Phase1"` with a lead paragraph.

