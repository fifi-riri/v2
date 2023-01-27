from fastapi import APIRouter
from sql_base.models import reader
import resolvers.book

book_router = APIRouter()


@reader_router.get('/')
def get_readers():
    return f'Response: {{text: Страница со списком авторов}}'


@reader_router.post('/')
def new_reader(reader: readers,):
    new_id = resolvers.reader.new_reader(reader)
    return f'{{code: 201, id: {new_id}}}'


@reader_router.get('/{reader_id}')
def get_reader(reader_id: int):
    reader = resolvers.get_reader(reader_id)
    return f'reader: {{FIO: ФИО Автора, id: {reader_id}}}'


@reader_router.put('/{reader_id}')
def update_reader(book_id: int):
    return f'Update reader {reader_id}'


@reader_router.delete('/{reader_id}')
def delelte_reader(reader_id: int):
    return f'delete reader {reader_id}'