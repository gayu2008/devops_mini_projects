from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo
from datetime import datetime
import os

app = Flask(__name__)

# Set up MongoDB URI and database name
app.config["MONGO_URI"] = "mongodb://localhost:27017/reminders_db"  # MongoDB URI
mongo = PyMongo(app)

# Task collection (equivalent to SQLAlchemy model in MongoDB)
tasks_collection = mongo.db.tasks

@app.route('/')
def index():
    tasks = tasks_collection.find()  # Fetch all tasks from the MongoDB collection
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task_name = request.form['task_name']
    reminder_time = request.form['reminder_time']
    reminder_time = datetime.strptime(reminder_time, "%Y-%m-%dT%H:%M")
    
    # Insert new task into MongoDB
    new_task = {
        'task_name': task_name,
        'reminder_time': reminder_time
    }
    tasks_collection.insert_one(new_task)
    
    return redirect(url_for('index'))

@app.route('/delete/<task_id>')
def delete_task(task_id):
    # Delete task by its MongoDB ObjectId
    tasks_collection.delete_one({'_id': mongo.db.ObjectId(task_id)})
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
