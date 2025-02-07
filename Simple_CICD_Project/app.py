from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_pymongo import PyMongo
from datetime import datetime
import threading
import time
from bson.objectid import ObjectId

app = Flask(__name__)

# MongoDB Configuration
app.config["MONGO_URI"] = "mongodb://localhost:27017/reminders_db"
mongo = PyMongo(app)
tasks_collection = mongo.db.tasks

# Background thread to check for reminders
def check_reminders():
    while True:
        now = datetime.now()
        tasks = tasks_collection.find()
        for task in tasks:
            reminder_time = task.get('reminder_time')
            if reminder_time and reminder_time <= now:
                print(f"Reminder: {task['task_name']} is due!")
                tasks_collection.delete_one({'_id': task['_id']})  # Auto-delete after notification
        time.sleep(60)  # Check every minute

# Start background thread
threading.Thread(target=check_reminders, daemon=True).start()

@app.route('/')
def index():
    tasks = tasks_collection.find()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task_name = request.form['task_name']
    reminder_time = request.form['reminder_time']
    reminder_time = datetime.strptime(reminder_time, "%Y-%m-%dT%H:%M")

    new_task = {'task_name': task_name, 'reminder_time': reminder_time}
    tasks_collection.insert_one(new_task)
    
    return redirect(url_for('index'))

@app.route('/delete/<task_id>', methods=['POST'])
def delete_task(task_id):
    tasks_collection.delete_one({'_id': ObjectId(task_id)})
    return jsonify({'message': 'Task deleted'})

# New API to fetch reminders dynamically
@app.route('/get_reminders', methods=['GET'])
def get_reminders():
    now = datetime.now()
    due_tasks = tasks_collection.find({"reminder_time": {"$lte": now}})
    
    reminders = []
    for task in due_tasks:
        reminders.append({"_id": str(task["_id"]), "task_name": task["task_name"]})
        tasks_collection.delete_one({"_id": task["_id"]})  # Auto-delete after notification

    return jsonify(reminders)

if __name__ == '__main__':
    app.run(debug=True)
