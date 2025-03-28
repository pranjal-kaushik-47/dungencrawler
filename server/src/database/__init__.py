import os
from mongoengine import connect

from .user import (
    User
)

connect(host=os.environ.get('db'))