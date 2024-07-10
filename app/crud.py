from .database import users_collection
from .models import User

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

def get_task(task):
    return {
        'task_id': str(task['_id']),
        'title': task['title'],
        'description': task['description'],
        'priority': task['priority'],
        'category': task['category'],
        'completed': task['completed']
    }