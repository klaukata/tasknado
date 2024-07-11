from fastapi import APIRouter, Depends
from ..database import tasks_collection
from ..auth import o2auth_scheme, decode_token
from ..schemas import TaskCreate, TaskEdit
from ..crud import list_tasks, insert_task, update_task, del_task

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
    return insert_task(owner_username, task_dict)

@router.put('/edit')
def edit_task(task_id: str, task: TaskEdit, token: str = Depends(o2auth_scheme)):
    owner_username = decode_token(token)
    return update_task(owner_username, task_id, task.model_dump())
    
@router.delete('/delete')
def remove_task(task_id, token: str = Depends(o2auth_scheme)):
    owner_username = decode_token(token)
    return del_task(owner_username, task_id)
