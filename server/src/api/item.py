from fastapi import APIRouter
from pydantic import BaseModel
from typing import Dict, Any

from ..database import (
    ItemTypes,
    Item
)


router = APIRouter(prefix='/item')

class ItemTypePayload(BaseModel):
    name: str
    icon: str
    meta_data: Dict[str, Any]

@router.post('/type/create')
async def itemtypepost(item_type: ItemTypePayload):
    print(item_type, flush=True)
    it = ItemTypes(
        name=item_type.name,
        icon=item_type.icon,
        meta_data=item_type.meta_data
    ).save()
    data = it.to_mongo().to_dict()
    return {**data, '_id': str(it.id)}

@router.get('/')
async def test():
    return {}