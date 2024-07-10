from fastapi import HTTPException
from bson import ObjectId
from .database import users_collection, tasks_collection
from .models import User

no_task_exception = HTTPException(
    status_code=404,
    detail='Task not found. Enter a correct task_id'
)
not_owner_exception = HTTPException(
    status_code=403,
    detail="You're trying to mess with a task that is not yours. Not cool."
)

# auth related
def get_user(username: str):
    user_doc = users_collection.find_one({'username': username})
    return User(**user_doc) if user_doc else None

def create_user(user_details: User):
    users_collection.insert_one(dict(user_details))
    return {
        'details': 'User created!'
    }

# user related
def display_user_details(user: User):
    return {
        'Your username': user.username,
        'Your email': user.email
    }

# task related
def list_tasks(cursor) -> list:
    return [get_task(task) for task in cursor]

def get_task(task) -> dict:
    return {
        'task_id': str(task['_id']),
        'title': task['title'],
        'description': task.get('description'),
        'priority': task['priority'],
        'category': task.get('category'),
        'completed': task.get('completed')
    }

def insert_task(username: str, task: dict):
    task['completed'] = False
    task['owner'] = username
    tasks_collection.insert_one(task)
    return {
        'details': 'Task added!'
    }

def validate_user_and_task(username: str, task_id: str):
    task_doc = tasks_collection.find_one({'_id': ObjectId(task_id)})
    if task_doc is None:
        raise no_task_exception
    task_username = task_doc['owner']
    if task_username != username:
        raise not_owner_exception
    return True

def update_task(username: str, task_id: str, task: dict):
    if validate_user_and_task(username, task_id):
        tasks_collection.find_one_and_update({'_id': ObjectId(task_id)}, {'$set': task})
        return {
            'details': 'Task updated!'
        }
    return {
        'details': 'Task not updated'
    }

def del_task(username: str, task_id: str):
    if validate_user_and_task(username, task_id):
        tasks_collection.find_one_and_delete({'_id': ObjectId(task_id)})
        return {
            'detail': 'Task removed!'
        }
    else:
        return {
            'detail': 'Task not removed'
        }