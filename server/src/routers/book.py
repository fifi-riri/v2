from fastapi import APIRouter
from sql_base.models import book
import resolvers.book

book_router = APIRouter()


@book_router.get('/')
def get_books():
    return f'Response: {{text: Страница со списком студентов}}'


@book_router.post('/')
def new_books(book: books,):
    new_id = resolvers.books.new_book(book)
    return f'{{code: 201, id: {new_id}}}'


@book_router.get('/{ищщл_id}')
def get_books(book_id: int):
    book = resolvers.get_book(book_id)
    return f'book: {{name: название книги, id: {book_id}}}'


@book_router.put('/{book_id}')
def update_book(book_id: int):
    return f'Update book {book_id}'


@book_router.delete('/{book_id}')
def delelte_book(book_id: int):
    return f'delete book {book_id}'