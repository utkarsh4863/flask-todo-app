# 📝 To-Do List App

A simple **To-Do List web application** built with **Flask**, **SQLAlchemy**, and **Flask-Login**.  
Users can register, login, create tasks, mark them as complete, delete tasks, and track progress.  
The app features a clean dashboard, dark mode, and user profiles with task statistics.

---

## 🛠 Features

- **User Authentication:** Register, login, logout with secure password hashing.  
- **Task Management:** Add, update, complete, and delete tasks.  
- **Task Filtering:** Filter tasks by status (completed/pending).  
- **User Profile:** View personal task stats and activity.  
- **Responsive UI:** Clean, mobile-friendly dashboard.  
- **Dark Mode Toggle:** Switch between light and dark themes.

---

## ⚡ Installation

Follow these steps to set up the project locally:

1. Clone the repository:

git clone https://github.com/utkarsh4863/flask-todo-app
cd flask-todo-app

2. Create a virtual environment:

python -m venv venv

3. Activate the virtual environment:

- Windows:
venv\Scripts\activate

- macOS/Linux:
source venv/bin/activate

4. Install dependencies:

pip install -r requirements.txt

5. Run the application:

python run.py

---

## 📦 Dependencies

This project requires the following Python packages:

- **Flask** - Web framework for building the application.  
- **Flask-Login** - User session management for Flask.  
- **Flask-SQLAlchemy** - ORM for database interactions.  
- **Werkzeug** - Utility library, used here for password hashing.  

All dependencies are listed in `requirements.txt`.

---

## 🖼 Screenshots

![Dashboard](https://github.com/utkarsh4863/flask-todo-app/blob/main/To%20do%20app%20screenshots.png)

---

## 📌 Notes

- The SQLite database (`todo.db`) is auto-created in the `instance/` folder.  
- Dark mode preferences are stored locally in the browser.  
- Make sure the `venv/` and `instance/` folders are ignored in GitHub (`.gitignore`).

---







