from typing import Dict, List

from ulid import ulid

from todoberry.db import ListsDB, ItemsDB
from todoberry.models import ItemsList, Item


def _to_model(model, data: Dict):
    """
    creates a BaseModel instance from a dict of fields.
    convert _id to id, because BaseModel ignores fields with leading underscore
    """
    return model(
        **{'id' if k == '_id' else k: str(v) if k == '_id' else v for k, v in
           data.items()}
    )


class ListService:
    @classmethod
    def get_lists(cls) -> List[ItemsList]:
        return [_to_model(ItemsList, list_) for list_ in ListsDB.get_all()]

    @classmethod
    def get_list(cls, list_id: str) -> ItemsList:
        list_ = _to_model(ItemsList, ListsDB.get(list_id))
        list_.items = ItemService.get_items(list_id)

        return list_

    @classmethod
    def create_list(cls, obj: ItemsList) -> ItemsList:
        data = obj.dict()
        data['_id'] = str(ulid())
        return _to_model(ItemsList, ListsDB.insert(data))

    @classmethod
    def update_list(cls, list_id: str, obj: ItemsList) -> ItemsList:
        data = obj.dict()
        data['_id'] = list_id
        del data['id']

        return _to_model(ItemsList, ListsDB.update(list_id, data))

    @classmethod
    def delete_list(cls, list_id: str):
        ListsDB.delete(list_id)
        ItemService.delete_list_items(list_id)


class ItemService:
    @classmethod
    def get_items(cls, list_id: str) -> [Item]:
        return [
            _to_model(Item, item)
            for item in ItemsDB.get_by_fk('_list_id', list_id)
        ]

    @classmethod
    def get_item(cls, item_id: str) -> [Item]:
        return _to_model(Item, ItemsDB.get(item_id))

    @classmethod
    def create_item(cls, list_id: str, obj: Item) -> [Item]:
        data = obj.dict()
        data['_id'] = str(ulid())
        data['_list_id'] = list_id
        return _to_model(Item, ItemsDB.insert(data))

    @classmethod
    def update_item(cls, item_id: str, obj: Item) -> [Item]:
        data = obj.dict()
        data['_id'] = item_id
        del data['id']

        return _to_model(Item, ItemsDB.update(item_id, data))

    @classmethod
    def delete_item(cls, item_id: str):
        ItemsDB.delete(item_id)

    @classmethod
    def delete_list_items(cls, list_id: str):
        ItemsDB.delete_many('_list_id', list_id)
