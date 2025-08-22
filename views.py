from fastapi import APIRouter



router = APIRouter()

@router.get('/', tags=['welcome page'])
def welcome():
    return {
        'Message': 'Hello, we are pleased to welcome you to the quotes app'
    }









