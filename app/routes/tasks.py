from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from app import db
from app.models import Task
from datetime import datetime

tasks = Blueprint('tasks', __name__)

@tasks.route('/')
@login_required
def dashboard():
    search = request.args.get('search')
    priority_filter = request.args.get('priority')
    query = Task.query.filter_by(user_id=current_user.id)

    if search:
        query = query.filter(Task.title.contains(search))
    if priority_filter and priority_filter != "All":
        query = query.filter_by(priority=priority_filter)

    all_tasks = query.all()
    return render_template('tasks.html', tasks=all_tasks)

@tasks.route('/add', methods=['POST'])
@login_required
def add_task():
    title = request.form.get('title')
    due_date = request.form.get('due_date')
    priority = request.form.get('priority')

    if title:
        new_task = Task(
            title=title,
            due_date=datetime.strptime(due_date, "%Y-%m-%d") if due_date else None,
            priority=priority,
            user_id=current_user.id
        )
        db.session.add(new_task)
        db.session.commit()
        flash("Task added!", "success")
    return redirect(url_for('tasks.dashboard'))

@tasks.route('/complete/<int:task_id>')
@login_required
def complete_task(task_id):
    task = Task.query.get_or_404(task_id)
    if task.user_id == current_user.id:
        task.completed = True
        db.session.commit()
    return redirect(url_for('tasks.dashboard'))

@tasks.route('/delete/<int:task_id>')
@login_required
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    if task.user_id == current_user.id:
        db.session.delete(task)
        db.session.commit()
    return redirect(url_for('tasks.dashboard'))

@tasks.route('/profile')
@login_required
def profile():
    total = Task.query.filter_by(user_id=current_user.id).count()
    completed = Task.query.filter_by(user_id=current_user.id, completed=True).count()
    pending = total - completed
    return render_template("profile.html", total=total, completed=completed, pending=pending)
