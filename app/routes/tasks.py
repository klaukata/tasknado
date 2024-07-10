from fastapi import APIRouter, Depends
from ..database import tasks_collection
from ..token import o2auth_scheme, decode_token
from ..schemas import TaskCreate, TaskEdit
from ..crud import list_tasks

router = APIRouter()

@router.get('/')
def get_tasks(token: str = Depends(o2auth_scheme)):
    owner_username = decode_token(token)
    tasks_cursor = tasks_collection.find({'owner': owner_username})
    return list_tasks(tasks_cursor)
    


@router.post('/create')
def create_task(task: TaskCreate, token: str = Depends(o2auth_scheme)):
    owner_username = decode_token(token)
    task_dict = task.model_dump()
    task_dict['completed'] = False
    task_dict['owner'] = owner_username
    tasks_collection.insert_one(task_dict)
    return {
        'details': 'Task added!'
    }

@router.put('/edit')
def edit_task():
    pass