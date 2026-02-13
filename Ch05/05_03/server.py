from http import HTTPStatus

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel

try:
    # Prefer package-style relative import when running as a module
    from . import users
except Exception:
    # Fall back to plain import when running server.py directly
    import users

app = FastAPI()


@app.get('/users/{login}')
def get_user(login: str):
    user = users.get(login)
    if user is None:
        return JSONResponse(
            status_code=HTTPStatus.NOT_FOUND,
            content={'error': f'{login!r} not found'},
        )

    return user


class User(BaseModel):
    login: str
    uid: int
    name: str
    is_admin: bool


@app.post('/users/{login}')
def set_user(login, user: User):
    users.set(login, user.model_dump())
    return {
        'error': None,
        'login': user.login,
    }


@app.post('/users/{login}/icon')
async def set_icon(login: str, request: Request):
    user = users.get(login)
    if user is None:
        return JSONResponse(
            status_code=HTTPStatus.NOT_FOUND,
            content={'error': f'{login!r} not found'},
        )

    data = await request.body()
    user['icon'] = data
    users.set(login, user)

    return {
        'error': None,
        'login': login,
    }
