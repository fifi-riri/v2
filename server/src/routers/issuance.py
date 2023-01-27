from fastapi import APIRouter
from sql_base.models import issuance
import resolvers.issuance

issuance_router = APIRouter()


@issuance_router.get('/')
def get_issuances():
    return f'Response: {{text: Страница со списком issuance}}'


@issuance_router.post('/')
def new_issuances(issuance: issuances,):
    new_id = resolvers.issuances.new_issuance(issuance)
    return f'{{code: 201, id: {new_id}}}'


@issuance_router.get('/{stud_id}')
def get_issuances(issuance_id: int):
    issuance = resolvers.get_issuance(issuance_id)
    return f'issuance: {{ id: {issuance_id}}}'


@issuance_router.put('/{issuance_id}')
def update_issuance(issuance_id: int):
    return f'Update issuance {issuance_id}'


@issuance_router.delete('/{issuance_id}')
def delelte_issuance(issuance_id: int):
    return f'delete issuance {issuance_id}'