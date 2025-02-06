# # from flask import Flask, render_template, request, redirect, url_for
# # from flask_sqlalchemy import SQLAlchemy
# # from datetime import datetime, timedelta
# # import os

# # app = Flask(__name__)
# # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reminders.db'
# # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# # db = SQLAlchemy(app)

# # class Task(db.Model):
# #     id = db.Column(db.Integer, primary_key=True)
# #     task_name = db.Column(db.String(100), nullable=False)
# #     reminder_time = db.Column(db.DateTime, nullable=False)

# #     def __repr__(self):
# #         return f"<Task {self.task_name}>"

# # @app.route('/')
# # def index():
# #     tasks = Task.query.all()
# #     return render_template('index.html', tasks=tasks)

# # @app.route('/add', methods=['POST'])
# # def add_task():
# #     task_name = request.form['task_name']
# #     reminder_time = request.form['reminder_time']
# #     reminder_time = datetime.strptime(reminder_time, "%Y-%m-%dT%H:%M")
    
# #     new_task = Task(task_name=task_name, reminder_time=reminder_time)
# #     db.session.add(new_task)
# #     db.session.commit()
    
# #     return redirect(url_for('index'))

# # @app.route('/delete/<int:id>')
# # def delete_task(id):
# #     task = Task.query.get_or_404(id)
# #     db.session.delete(task)
# #     db.session.commit()
    
# #     return redirect(url_for('index'))

# # if __name__ == '__main__':
# #     if not os.path.exists('reminders.db'):
# #         db.create_all()
# #     app.run(debug=True)

# from flask import Flask, render_template, request, redirect, url_for
# from flask_pymongo import PyMongo
# from datetime import datetime
# import os

# app = Flask(__name__)

# # Set up MongoDB URI and database name
# app.config["MONGO_URI"] = "mongodb://localhost:27017/reminders_db"  # MongoDB URI
# mongo = PyMongo(app)

# # Task collection (equivalent to SQLAlchemy model in MongoDB)
# tasks_collection = mongo.db.tasks

# @app.route('/')
# def index():
#     tasks = tasks_collection.find()  # Fetch all tasks from the MongoDB collection
#     return render_template('index.html', tasks=tasks)

# @app.route('/add', methods=['POST'])
# def add_task():
#     task_name = request.form['task_name']
#     reminder_time = request.form['reminder_time']
#     reminder_time = datetime.strptime(reminder_time, "%Y-%m-%dT%H:%M")
    
#     # Insert new task into MongoDB
#     new_task = {
#         'task_name': task_name,
#         'reminder_time': reminder_time
#     }
#     tasks_collection.insert_one(new_task)
    
#     return redirect(url_for('index'))

# @app.route('/delete/<task_id>')
# def delete_task(task_id):
#     # Delete task by its MongoDB ObjectId
#     tasks_collection.delete_one({'_id': mongo.db.ObjectId(task_id)})
    
#     return redirect(url_for('index'))

# if __name__ == '__main__':
#     app.run(debug=True)
