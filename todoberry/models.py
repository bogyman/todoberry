from datetime import datetime
from typing import List

from pydantic import BaseModel


class Item(BaseModel):
    id: str = ''
    name: str
    due_date: datetime = None
    finished: bool


class ItemsList(BaseModel):
    id: str = ''
    name: str
    items: List[Item] = []
