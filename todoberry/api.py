from typing import List

from fastapi import APIRouter

from todoberry.models import Item, ItemsList
from todoberry.services import ItemService, ListService

items_router = APIRouter()
lists_router = APIRouter()


@items_router.get("/", response_model=Item)
def get_items(list_id: str):
    return ItemService.get_items(list_id)


@items_router.get("/{item_id}", response_model=Item)
def get_item(item_id: str):
    return ItemService.get_item(item_id)


@items_router.post("/", response_model=Item)
def create_item(list_id: str, item: Item):
    return ItemService.create_item(list_id, item)


@items_router.put("/{item_id}", response_model=Item)
def update_item(item_id: str, item: Item):
    return ItemService.update_item(item_id, item)


@items_router.delete("/{item_id}", response_model=Item)
def delete_item(item_id: str):
    ItemService.delete_item(item_id)


@lists_router.get("/", response_model=List[ItemsList])
def get_lists():
    return ListService.get_lists()


@lists_router.get("/{list_id}", response_model=ItemsList)
def get_list(list_id: str):
    return ListService.get_list(list_id)


@lists_router.post("/", response_model=ItemsList)
def create_list(list_: ItemsList):
    return ListService.create_list(list_)


@lists_router.put("/{list_id}", response_model=ItemsList)
def update_list(list_id: str, list_: ItemsList):
    return ListService.update_list(list_id, list_)


@lists_router.delete("/{list_id}")
def delete_list(list_id: str):
    ListService.delete_list(list_id)
