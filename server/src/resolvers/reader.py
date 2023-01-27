from sql_base import base_worker
from sql_base import models


def new_reader(reader: models.Readers) -> int:
    new_id = base_worker.execute("INSERT INTO readers(FIO) "
                                     "VALUES(?) "
                                     "RETURNING id",
                                     (reader.FIO))
    return new_id