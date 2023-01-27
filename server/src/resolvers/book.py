from sql_base import base_worker
from sql_base import models


def new_book(book: models.books) -> int:
    new_id = base_worker.execute("INSERT INTO book(name) "
                                     "VALUES(?) "
                                     "RETURNING id",
                                     (book.name))
    return new_id