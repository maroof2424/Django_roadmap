## 📅 **Django Full-Stack Backend Roadmap**

**Duration:** 60 Days
**Daily Time:** 1.5–2 Hours
**Start Date Example:** July 20, 2025
**Structure:**

* 🧠 **Mon–Fri:** Concept + Practice
* 🔁 **Saturday:** Task/Project Day
* 🧪 **Sunday:** Practice/Revision

---

### 🔰 **Phase 1: Django Fundamentals (Day 1–14)**

> Goal: Understand core Django structure, views, templates, models, static/media handling.

| Day | Topics                                                                | Practice / Task                          |
| --- | --------------------------------------------------------------------- | ---------------------------------------- |
| 1   | Setup: Python, pip, venv, install Django, `django-admin startproject` | Setup project + Explore folder structure |
| 2   | `settings.py`, `urls.py`, `views.py`, `templates`, `static`           | Create homepage with Bootstrap           |
| 3   | URLs, Views (Function-Based), Templates, Template Inheritance         | Create About, Contact pages              |
| 4   | Static & Media files, base layout, navbar/footer                      | Link static files + upload image         |
| 5   | Models, Migrations, Admin Panel intro                                 | Create `Product`, `Category` model       |
| 6   | Task Day                                                              | Build mini MyShop with admin management  |
| 7   | Practice/Revision                                                     | Create another model + template display  |
| 8   | Django Forms (Simple), form rendering                                 | Create product form                      |
| 9   | CRUD (Create, Read, Update, Delete)                                   | Implement CRUD for `Product` model       |
| 10  | Model relationships (OneToMany, ForeignKey), verbose\_name            | Add Category to Product                  |
| 11  | Custom admin, search/filter in admin                                  | Improve Admin Panel                      |
| 12  | Pagination, Messages, Redirects                                       | Paginate products                        |
| 13  | Task Day                                                              | Build full CRUD product manager          |
| 14  | Practice Day                                                          | Refactor & clean up                      |

---

### 🚀 **Phase 2: Django REST Framework (Day 15–26)**

> Goal: Learn API development, serializers, ViewSets, permissions, JWT auth.

| Day | Topics                                                             | Practice / Task                           |
| --- | ------------------------------------------------------------------ | ----------------------------------------- |
| 15  | Install `djangorestframework`, create API project, setup app       | Basic `/api/products` endpoint            |
| 16  | Serializers, JSON rendering, APIView                               | List & create `Product` via API           |
| 17  | ModelSerializer, status codes, Response object                     | Create-Update-Delete via DRF              |
| 18  | ViewSets & Routers (DefaultRouter)                                 | Refactor views with ViewSets              |
| 19  | Permissions (IsAuthenticated, AllowAny, IsAdmin)                   | Add permission control to API             |
| 20  | Task Day                                                           | Build mini CRUD API with auth + filtering |
| 21  | Practice Day                                                       | Add search filter                         |
| 22  | DRF Filtering, Searching, Ordering                                 | Search products by name, sort by price    |
| 23  | DRF Pagination, nested serializers                                 | Paginate results + show category info     |
| 24  | Django CORS headers (`django-cors-headers`)                        | Add CORS support for frontend integration |
| 25  | Token Auth vs JWT – Setup JWT with `djangorestframework-simplejwt` | Add Login/Refresh token endpoints         |
| 26  | Task Day                                                           | Build token-protected API                 |

---

### ⚙️ **Phase 3: Django Essentials + 3rd Party Tools (Day 27–41)**

> Goal: Use essential libraries for modern development & API documentation.

| Day | Topics                                               | Practice / Task                                  |
| --- | ---------------------------------------------------- | ------------------------------------------------ |
| 27  | `.env` files, install & setup `django-environ`       | Move all secrets to `.env`                       |
| 28  | Handling static files with `whitenoise`              | Setup whitenoise for production                  |
| 29  | API Docs: `drf-yasg` or `drf-spectacular`            | Generate Swagger/OpenAPI docs                    |
| 30  | Custom User Model (AbstractBaseUser vs AbstractUser) | Create custom `User` model                       |
| 31  | Signals (post\_save, pre\_save)                      | Auto-create profile after user registration      |
| 32  | `django-allauth` intro + install                     | Setup login, signup, password reset              |
| 33  | Social Login (Google or GitHub) via `django-allauth` | Implement OAuth login                            |
| 34  | Task Day                                             | Integrate `allauth`, `env`, `whitenoise`, `CORS` |
| 35  | Practice Day                                         | API doc update + Social login testing            |
| 36  | Unit Testing: `unittest`, structure                  | Write tests for Product CRUD                     |
| 37  | Pytest + `pytest-django`                             | Convert to pytest, run tests                     |
| 38  | Coverage reports, mock tests                         | Add test coverage and run                        |
| 39  | Docker Basics (optional): Dockerfile, docker-compose | Containerize Django app                          |
| 40  | Task Day                                             | Dockerize full project                           |
| 41  | Practice/Debug Day                                   | Fix issues & polish                              |

---

### 💼 **Phase 4: Project + Deployment (Day 42–60)**

> Goal: Complete real-world Django REST project & deploy on Render/Heroku.

| Day   | Topics                                                                               | Practice / Task                      |
| ----- | ------------------------------------------------------------------------------------ | ------------------------------------ |
| 42    | Project Planning: eCommerce, Blog API, Portfolio CMS (choose 1)                      | Design models, routes                |
| 43    | Full DB schema + serializers                                                         | Create models, serializers           |
| 44    | Views, Pagination, Filtering                                                         | Build product listing and detail API |
| 45    | JWT Auth, Permissions, Custom User                                                   | Add auth system                      |
| 46    | Cart/Wishlist logic                                                                  | Add cart API views                   |
| 47    | Orders, Checkout, Coupons                                                            | Finalize order flow                  |
| 48    | Admin Panel customization                                                            | Add filters, inline forms            |
| 49    | Add Swagger docs + CORS + Static env                                                 | Final QA check                       |
| 50    | Deployment with Render (or Heroku)                                                   | Push live project                    |
| 51    | Task Day                                                                             | Submit deployed project              |
| 52–60 | Bonus Days: Add features like: search, review system, vendor dashboard, image upload | Stretch goals + polishing            |

---

## 📦 Included Libraries & Where Used:

| Library                      | Usage                                           |
| ---------------------------- | ----------------------------------------------- |
| `rest_framework`             | Core API functionality                          |
| `django-environ`             | Secure environment variable handling            |
| `whitenoise`                 | Serve static files in production                |
| `django-cors-headers`        | Enable CORS to allow frontend access            |
| `drf-yasg` or `spectacular`  | API documentation with Swagger/OpenAPI          |
| `pytest-django` / `unittest` | Testing setup                                   |
| `django-allauth`             | Login, signup, email verification, social login |

