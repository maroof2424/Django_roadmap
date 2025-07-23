## 📅 Phase1 - Day 3: Pages with FBVs + Template Inheritance

### ✅ Objective:

* Create **About** and **Contact** pages using function-based views
* Use **template inheritance** to avoid repeating HTML
* Practice URL routing and `render()`

---

### 📁 Updated Folder Structure

```
phase1/
├── home/
│   ├── templates/
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── about.html
│   │   └── contact.html
```

---

### 🛠️ What Was Done Today

#### 1. **Created Base Template** (`base.html`)

```html
<!-- home/templates/base.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}Phase1{% endblock %}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="bg-dark text-white">
    <nav class="navbar navbar-expand-lg navbar-dark bg-black px-3">
        <a class="navbar-brand" href="/">Phase1</a>
        <div>
            <a class="nav-link text-white" href="/">Home</a>
            <a class="nav-link text-white" href="/about/">About</a>
            <a class="nav-link text-white" href="/contact/">Contact</a>
        </div>
    </nav>

    <div class="container mt-5">
        {% block content %}{% endblock %}
    </div>
</body>
</html>
```

---

#### 2. **Updated All Pages to Inherit from `base.html`**

**home.html**

```html
{% extends 'base.html' %}
{% block title %}Home - Phase1{% endblock %}
{% block content %}
    <h1 class="display-4 text-center">Welcome to Phase1</h1>
    <p class="lead text-center">This is your homepage using Django + Bootstrap only.</p>
{% endblock %}
```

**about.html**

```html
{% extends 'base.html' %}
{% block title %}About - Phase1{% endblock %}
{% block content %}
    <h1 class="text-center">About Us</h1>
    <p class="text-center">This is the About page.</p>
{% endblock %}
```

**contact.html**

```html
{% extends 'base.html' %}
{% block title %}Contact - Phase1{% endblock %}
{% block content %}
    <h1 class="text-center">Contact Us</h1>
    <p class="text-center">This is the Contact page.</p>
{% endblock %}
```

---

#### 3. **Updated `views.py`**

```python
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')
```

---

#### 4. **Updated `urls.py` (app-level)**

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
```

---

### ✅ Output Preview

* `/` — Homepage
* `/about/` — About Page
* `/contact/` — Contact Page
* All pages share `base.html` (DRY principle)

