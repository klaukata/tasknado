from fastapi import APIRouter, Depends, HTTPException
from bson import ObjectId
from ..database import tasks_collection
from ..token import o2auth_scheme, decode_token
from ..schemas import TaskCreate, TaskEdit
from ..crud import list_tasks, insert_task, del_task

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
def edit_task(task_id: str, task: TaskEdit, token: str = Depends(o2auth_scheme)): # TODO - move to crud
    owner_username = decode_token(token)
    try:
        task_doc = tasks_collection.find_one({'_id': ObjectId(task_id)})
    except:
        raise HTTPException(
            status_code=404,
            detail="Task not found. Enter a correct task_id"
        )
    if task_doc['owner'] != owner_username:
        raise HTTPException(
            status_code=403,
            detail='You are trying to edit a task that is not yours. Not cool.'
        )
    tasks_collection.find_one_and_update({'_id': ObjectId(task_id)}, {'$set': task.model_dump()})
    return {
        'details': 'Task updated! c:'
}
    
@router.delete('/delete')
def remove_task(task_id, token: str = Depends(o2auth_scheme)):
    owner_username = decode_token(token)
    return del_task(owner_username, task_id)
