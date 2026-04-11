# 🍵 Django Chai Store Project

A Django-based learning project built to practice core backend concepts like models, views, templates, forms, and database relationships.

---

## 🚀 Features

- View all chai varieties
- Detailed chai pages
- Store filtering based on chai variety
- Django admin panel for data management
- Form-based search system

---

## 🧠 Django Concepts Covered

### 📌 Models (ORM)
- One-to-Many Relationship (`Review → chaivarity`)
- Many-to-Many Relationship (`store ↔ chaivarity`, `Order ↔ chaivarity`)
- One-to-One Relationship (`Profile → User`)

### 📌 Views
- Function-Based Views (FBVs)
- `render()` for templates
- `get_object_or_404()` for safe queries
- GET & POST request handling

### 📌 Templates
- Template inheritance (`extends`)
- Template tags (`for`, `if`)
- Dynamic rendering of data

### 📌 Forms
- Django `ModelForm`
- `ModelChoiceField`
- Form validation handling

### 📌 URLs
- App-level routing
- Dynamic URLs with parameters

---

## 📂 Project Structure

## 📂 Project Structure


FirstDjango/
│
├── first/ # Main app
│ ├── models.py # Database models
│ ├── views.py # Business logic
│ ├── forms.py # Django forms
│ ├── urls.py # App routes
│ └── templates/ # HTML templates
│
├── FirstDjango/ # Project settings
│ ├── settings.py
│ ├── urls.py
│
├── db.sqlite3 # Database
└── manage.py


---

🌐 Routes
Route	Description
/	Home page
/first/	List chai varieties
/first/<id>/	Chai detail page
/first/chai_store/	Store filter page
🛠 Tech Stack
Python 3
Django 5+
SQLite
HTML (Django Templates)

📚 Learning Outcome

This project helped in understanding:

Django MVT architecture
ORM relationships
Template rendering
Form handling (GET/POST)
Admin panel usage
URL routing system


🔮 Future Improvements
Add authentication system
REST API (Django REST Framework)
AJAX filtering
UI improvements (Tailwind/Bootstrap)
User reviews system

👨‍💻 Author
Ujjwal Kumar Gupta
