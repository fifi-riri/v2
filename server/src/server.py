from fastapi import FastAPI
from sql_base import base_worker
from settings import BASE_PATH
from routers.autor import autor_router
from routers.book import book_router
from routers.readers import reader_pouter
from routers.staff import staff_pouter
from routers.issuance import issuance_pouter



base_worker.set_base_path(BASE_PATH)

if not base_worker.check_base():
    base_worker.create_base('../sql/base.sql')

app = FastAPI()


@app.get("/")
def main_page():
    return {'page': 'Connection in correct'}


app.include_router(autor_router, prefix='/autor')
app.include_router(book_router, prefix='/book')
app.include_router(reader_pouter, prefix='/readers')
app.include_router(staffr_pouter, prefix='/staff')
app.include_router(issuance_pouter, prefix='/issuance')



