from fastapi import FastAPI
from .routes.auth import router as auth_router
from .routes.users import router as users_router

app = FastAPI()

app.include_router(users_router, prefix='/users')
app.include_router(auth_router, prefix='/auth')


@app.get('/')
def read_root():
    return {
        'msg': 'hi from the root! c:'
    }