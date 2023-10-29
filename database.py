# Import necessary libraries
import sqlite3
from flask import Flask, request, jsonify

# Initialize the Flask app
app = Flask(__name__)

# Connect to the SQLite database
conn = sqlite3.connect('tasks.db')
cursor = conn.cursor()

# Create a table for tasks if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        description TEXT,
        completed BOOLEAN
    )
''')
conn.commit()

# API endpoint to create a task
@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    title = data['title']
    description = data.get('description', '')
    
    # Insert the new task into the database
    cursor.execute('INSERT INTO tasks (title, description, completed) VALUES (?, ?, 0)', (title, description))
    conn.commit()
    
    return jsonify({'message': 'Task created!'})

# API endpoint to get all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    cursor.execute('SELECT * FROM tasks')
    tasks = cursor.fetchall()
    
    # Convert the tasks to a list of dictionaries
    task_list = [{'id': task[0], 'title': task[1], 'description': task[2], 'completed': task[3]} for task in tasks]
    
    return jsonify(task_list)

if __name__ == '__main__':
    app.run(debug=True)
