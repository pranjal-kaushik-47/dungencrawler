from fastapi import APIRouter

router = APIRouter(prefix='/user')

@router.get('/')
def home():
    return {'a':1}