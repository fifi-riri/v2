from fastapi import APIRouter
from sql_base.models import User
from resolvers import users

user_pouter = APIRouter()


@user_pouter.get('/')
def not_login():
    return {"Message": "Login in system"}


@user_pouter.post('/login')
def check_login(user: User, ):
    post = users.check_login(user)
    if post:
        return {"code": 200, "message": "Login correct", 'post': post}
    else:
        return {"code": 401, "message": "Login incorrect, try again", 'post': None}
