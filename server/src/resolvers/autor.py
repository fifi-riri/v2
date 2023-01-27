from sql_base import base_worker
from sql_base import models


def new_autor(autor: models.Autors) -> int:
    new_id = base_worker.execute("INSERT INTO autors(FIO) "
                                     "VALUES(?) "
                                     "RETURNING id",
                                     (autor.FIO))
    return new_id