from fastapi import FastAPI
from .routes.auth import router as auth_router
from .routes.users import router as users_router
from .routes.tasks import router as task_router

app = FastAPI()

app.include_router(task_router, prefix='/task', tags=['Tasks'])
app.include_router(users_router, prefix='/users', tags=['Read User'])
app.include_router(auth_router, prefix='/auth', tags=['Authorization'])


@app.get('/', tags=['Welcome Message'])
def read_root():
    return {
        'msg': 'hi from the root! c:'
    }