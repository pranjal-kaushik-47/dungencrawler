from mongoengine import (
    Document, StringField, FloatField, DictField
)

class ItemTypes(Document):
    name = StringField(required=True)
    icon = StringField(required=True)
    meta_data = DictField()

class Item(Document):
    name = StringField(required=True)
    description = StringField(required=True)
    icon = StringField(required=True)
    item_type = DictField(required=True)
    weight = FloatField(required=True)
