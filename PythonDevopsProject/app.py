from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# In-memory "database" (could be extended to use a real database)
tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form.get('task')
    if task:
        tasks.append(task)  # Add task to the list
    return redirect('/')

@app.route('/delete/<task>')
def delete_task(task):
    if task in tasks:
        tasks.remove(task)  # Remove task from the list
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)

