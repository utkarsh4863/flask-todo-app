# 📝 To-Do List App

A simple **To-Do List web application** built with **Flask**, **SQLAlchemy**, and **Flask-Login**. Users can register, login, create tasks, mark them as complete, delete tasks, and track progress. The app features a clean dashboard, dark mode, and user profiles with task statistics.

## 🛠 Features

- **User Authentication:** Register, login, logout with secure password hashing.
- **Task Management:** Add, update, complete, and delete tasks.
- **Task Filtering:** Filter tasks by status (completed/pending).
- **User Profile:** View personal task stats and activity.
- **Responsive UI:** Clean, mobile-friendly dashboard.
- **Dark Mode Toggle:** Switch between light and dark themes.

## 📁 Project Structure


TO-DO-LIST-APP/
│── run.py # App entry point
│── requirements.txt # Dependencies (Flask, Flask-Login, SQLAlchemy etc.)
│── app/
│ │── init.py # Flask app factory & DB setup
│ │── models.py # User & Task database models
│ │
│ ├── routes/
│ │ │── init.py # Makes "routes" a Python package
│ │ │── auth.py # Login, register, logout routes
│ │ │── tasks.py # Task CRUD and profile routes
│ │
│ ├── templates/
│ │ │── base.html # Common layout (navbar, flash messages, dark mode)
│ │ │── login.html
│ │ │── register.html
│ │ │── tasks.html # Task dashboard (add, filter, list, complete, delete)
│ │ │── profile.html # User profile page (stats)
│ │
│ ├── static/
│ │ ├── css/style.css
│ │ ├── js/script.js
│ │ └── images/ # Optional images, icons, logos
│
│── venv/ # Virtual environment (ignore in GitHub)
│── instance/
│ └── todo.db # SQLite database (auto-created)
