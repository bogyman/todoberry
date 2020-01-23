from typing import Dict, Union

from pymongo import MongoClient

from todoberry.settings import AppConfig

client = MongoClient(AppConfig.MONGO_HOST)


class DB:
    def __init__(self, collection_name: str):
        db = client[AppConfig.MONGO_DB]
        self.collection_name = collection_name
        self.collection = db[self.collection_name]

    def insert(self, data: Dict):
        self.collection.insert_one(data)
        return data

    def get(self, pk: str):
        document = self.collection.find_one({'_id': {'$eq': pk}})

        return document

    def get_by_fk(self, fk_name: str, fk: str):
        results = []

        for document in self.collection.find({fk_name: {'$eq': fk}}):
            results.append(document)

        return results

    def get_all(self):
        results = []

        for document in self.collection.find():
            results.append(document)

        return results

    def delete_many(self, fk_name: str, fk: str):
        self.collection.delete_many({fk_name: {'$eq': fk}})

    def delete(self, pk: str):
        self.delete_many("_id", pk)

    def update(self, pk: str, data: Dict):
        self.collection.update_one({'_id': pk}, {'$set': data})
        return self.get(pk)


ItemsDB = DB(AppConfig.MONGO_ITEM_COLLECTION)
ListsDB = DB(AppConfig.MONGO_LIST_COLLECTION)
