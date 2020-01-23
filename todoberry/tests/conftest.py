import pytest


@pytest.fixture(scope="function")
def mongodb_(mongodb, mocker):
    """replace created collections with mocked db"""
    from todoberry.services import ItemsDB, ListsDB
    ItemsDB.collection = mongodb[ItemsDB.collection_name]
    ListsDB.collection = mongodb[ListsDB.collection_name]

    yield mongodb
