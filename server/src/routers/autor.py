from fastapi import APIRouter
from sql_base.models import Autor
import resolvers.autor

autor_router = APIRouter()


@autor_router.get('/')
def get_autors():
    return f'Response: {{text: Страница со списком авторов}}'


@autor_router.post('/')
def new_autor(autor: Autors,):
    new_id = resolvers.autors.new_autor(autor)
    return f'{{code: 201, id: {new_id}}}'


@autor_router.get('/{stud_id}')
def get_autor(autor_id: int):
    autor = resolvers.get_autor(autor_id)
    return f'autor: {{FIO: фамилия имя автора, id: {autor_id}}}'


@autor_router.put('/{aitor_id}')
def update_autor(autor_id: int):
    return f'Update autor {autor_id}'


@stud_router.delete('/{stud_id}')
def delelte_student(stud_id: int):
    return f'delete student {stud_id}'