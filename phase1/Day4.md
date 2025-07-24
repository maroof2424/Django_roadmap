## ✅ **Day 4 - Static & Media Files | Base Layout | Navbar/Footer**

📌 **Goals:**

* Configure static and media files
* Create base layout (`base.html`)
* Include reusable `navbar.html` and `footer.html`
* Link CSS, JS, and images via static
* Upload and display an image from the media folder

---

### 🔧 1. **settings.py Configurations**

```python
import os

# Static files (CSS, JS)
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# Media files (User-uploaded)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

---

### 🧭 2. **urls.py Configuration (Project level)**

```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # your paths...
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

---

### 🗂️ 3. **Folder Structure**

```
phase1/
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── script.js
│
├── media/
│   └── uploads/
│       └── your-image.jpg
│
└── templates/
    ├── base.html
    ├── home.html
    ├── about.html
    └── contact.html
```

---

### 🧩 4. **base.html (with navbar & footer)**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}Phase1{% endblock %}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
</head>
<body class="bg-dark text-white">

    {% include 'navbar.html' %}
    
    <div class="container mt-4">
        {% block content %}{% endblock %}
    </div>

    {% include 'footer.html' %}
    <script src="{% static 'js/script.js' %}"></script>
</body>
</html>
```

---

### 🔗 5. **navbar.html & footer.html**

```html
<!-- navbar.html -->
<nav class="navbar navbar-expand-lg navbar-dark bg-primary">
  <div class="container-fluid">
    <a class="navbar-brand" href="/">Phase1</a>
    <div class="collapse navbar-collapse">
      <ul class="navbar-nav">
        <li class="nav-item"><a class="nav-link" href="{% url 'home' %}">Home</a></li>
        <li class="nav-item"><a class="nav-link" href="{% url 'about' %}">About</a></li>
        <li class="nav-item"><a class="nav-link" href="{% url 'contact' %}">Contact</a></li>
      </ul>
    </div>
  </div>
</nav>
```

```html
<!-- footer.html -->
<footer class="text-center mt-5">
    <hr>
    <p>&copy; 2025 Phase1 Project | Made with ❤️ by Maroof</p>
</footer>
```

---

### 🖼️ 6. **Image Upload & Display (Sample)**

```html
<!-- inside home.html -->
{% extends 'base.html' %}
{% block content %}
    <h1>Welcome!</h1>
    <img src="{{ MEDIA_URL }}uploads/your-image.jpg" class="img-fluid" alt="Demo">
{% endblock %}
```

OR dynamically (if using model image field):

```html
<img src="{{ object.image.url }}" alt="Uploaded" />
```

---

### ✅ Practice Tasks

* [x] Configure `STATICFILES_DIRS`, `MEDIA_ROOT`, `MEDIA_URL`
* [x] Create `base.html` layout with Bootstrap
* [x] Build `navbar.html` and `footer.html` and include them
* [x] Add custom `style.css` and test with a color change
* [x] Upload and show an image from the media folder

---