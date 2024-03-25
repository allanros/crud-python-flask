from flask import Flask, request, jsonify
from models.task import Task

# __name__ = __main__
app = Flask(__name__)

tasks = []
task_id_control = 1

@app.route('/tasks', methods=['POST'])
def create_task():
    global task_id_control
    data = request.get_json()
    new_task = Task(task_id_control, data['title'], data.get('description', ''))
    task_id_control += 1
    tasks.append(new_task)
    print(tasks)
    return jsonify({'message': 'Task created successfully', 'id': new_task.task_id})

@app.route('/tasks', methods=['GET'])
def list_tasks():
    task_list = [task.to_dict() for task in tasks]
    output = {
        'tasks': task_list,
        'total_tasks': len(task_list)
    }
    return jsonify(output)

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    for task in tasks:
        if task.task_id == task_id:
            return jsonify(task.to_dict())
    return jsonify({'message': 'Task not found'}), 404

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    for task in tasks:
        if task.task_id == task_id:
            print(task.to_dict())
            task.update_task(data['title'], data.get('description', ''), data.get('completed', False))
            print(task.to_dict())
            return jsonify({'message': 'Task updated successfully', 'id': task.task_id}), 200
    return jsonify({'message': 'Task not found'}), 404

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    for task in tasks:
        if task.task_id == task_id:
            tasks.remove(task)
            return jsonify({'message': 'Task deleted successfully'})
    return jsonify({'message': 'Task not found'}), 404

if __name__ == "__main__":
    app.run(debug=True)