from sql_base import base_worker
from sql_base import models


def new_staff(staff: models.Staffs) -> int:
    new_id = base_worker.execute("INSERT INTO staffs(FIO_S) "
                                     "VALUES(?) "
                                     "RETURNING id",
                                     (staff.FIO_S))
    return new_id