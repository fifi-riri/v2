from fastapi import APIRouter
from sql_base.models import staff
import resolvers.staff

staff_router = APIRouter()


@staff_router.get('/')
def get_staffs():
    return f'Response: {{text: Страница со списком персонала}}'


@staff_router.post('/')
def new_staffs(staff: staffs,):
    new_id = resolvers.staffs.new_staff(staff)
    return f'{{code: 201, id: {new_id}}}'


@staff_router.get('/{staff_id}')
def get_staffs(staff_id: int):
    staff = resolvers.get_staff(staff_id)
    return f'book: {{FIO_S: ФИО персонала, id: {staff_id}}}'


@staff_router.put('/{staff_id}')
def update_staff(staff_id: int):
    return f'Update staff {staff_id}'


@staff_router.delete('/{staff_id}')
def delelte_staff(staff_id: int):
    return f'delete staff {staff_id}'