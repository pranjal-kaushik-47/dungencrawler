from fastapi import APIRouter
from bson import ObjectId

from ..database import User

router = APIRouter(prefix='/user')

@router.get('/create')
def home():
    User(
        email='ross@example.com',
        first_name='Ross',
        last_name='Lawley'
    ).save()
    return {}

@router.get('/list')
def home():
    users = User.objects()
    users_serialized = [
        {**user.to_mongo().to_dict(), '_id': str(user.id)} for user in users
    ]
    return users_serialized