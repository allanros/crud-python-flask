import pytest
import requests

BASE_URL = 'http://localhost:5000'
tasks = []

# teste de criação de tarefa
def test_create_task():
    new_task_data = {
        'title': 'Task 1',
        'description': 'Task 1 description'
    }

    response = requests.post(f'{BASE_URL}/tasks', json=new_task_data)
    assert response.status_code == 200
    assert 'message' in response.json()
    assert 'id' in response.json()
    tasks.append(response.json()['id'])

# teste de listagem de tarefas
def test_list_tasks():
    response = requests.get(f'{BASE_URL}/tasks')
    assert response.status_code == 200
    assert 'tasks' in response.json()
    assert 'total_tasks' in response.json()

# teste de tarefa específica
def test_get_task():
    response = requests.get(f'{BASE_URL}/tasks/{tasks[0]}')
    assert response.status_code == 200
    assert 'title' in response.json()
    assert response.json()['id'] == tasks[0]
    assert 'description' in response.json()
    assert 'completed' in response.json()

# teste de atualização de tarefa
def test_update_task():
    if tasks:
        task_id = tasks[0]
        payload = {
            'title': 'Task 1 updated',
            'description': 'Task 1 description updated',
            'completed': False
        }

        response = requests.put(f'{BASE_URL}/tasks/{task_id}', json=payload)
        response.status_code == 200
        assert 'message' in response.json()
        assert response.json()['id'] == tasks[0]

        response = requests.get(f'{BASE_URL}/tasks/{task_id}')
        assert response.status_code == 200
        assert response.json()['title'] == payload['title']
        assert response.json()['description'] == payload['description']
        assert response.json()['completed'] == payload['completed']

# teste de remoção de tarefa
def test_delete_task():
    if tasks:
        task_id = tasks[0]
        response = requests.delete(f'{BASE_URL}/tasks/{task_id}')
        response.status_code == 200
        assert 'message' in response.json()

        response = requests.get(f'{BASE_URL}/tasks/{task_id}')
        assert response.status_code == 404