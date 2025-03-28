from fastapi import APIRouter

router = APIRouter(prefix='/inventory')

@router.get('/')
def home():
    return {}