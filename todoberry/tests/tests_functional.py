from starlette.testclient import TestClient

from todoberry.app import app

client = TestClient(app)


def test_get_lists(mongodb_):
    response = client.get("/lists/")
    assert response.status_code == 200
    assert response.json() == [
        {
            'id': '$list1',
            'name': 'List1',
            'items': []
        },
        {
            'id': '$listwithutitem',
            'name': 'ListWithutItem',
            'items': []
        },
        {
            'id': '$list2',
            'name': 'List2',
            'items': []
        }
    ]


def test_get_list(mongodb_):
    response = client.get("/lists/$list1")
    assert response.status_code == 200
    assert response.json() == {
        'id': '$list1',
        'items': [
            {
              'due_date': '2019-12-04T12:13:00',
              'finished': True,
              'id': '$item1',
              'name': 'item1'
            },
            {
              'due_date': '2019-12-05T12:13:00',
              'finished': True,
              'id': '$item3',
              'name': 'item3'
            }
        ],
        'name': 'List1'
    }


def test_create_list(mongodb_, mocker):
    mocker.patch('todoberry.services.ulid', return_value='rererer')
    response = client.post("/lists/", json={'name': "ListN"})
    assert response.status_code == 200
    assert response.json() == {
        'id': 'rererer',
        'items': [],
        'name': 'ListN'
    }


def test_update_list(mongodb_):
    response = client.put("/lists/$list1", json={'name': "ListN"})
    assert response.status_code == 200
    assert response.json() == {
        'id': '$list1',
        'items': [],
        'name': 'ListN'
    }


def test_delete_list(mongodb_):
    assert mongodb_.lists.find_one({'_id': {'$eq': '$list1'}}) is not None
    assert mongodb_.items.find_one({'_list_id': {'$eq': '$list1'}}) is not None

    response = client.delete("/lists/$list1")
    assert response.status_code == 200
    assert mongodb_.lists.find_one({'_id': {'$eq': '$list1'}}) is None
    assert mongodb_.items.find_one({'_list_id': {'$eq': '$list1'}}) is None


def test_create_item(mongodb_, mocker):
    mocker.patch('todoberry.services.ulid', return_value='rererer')
    response = client.post("/lists/$list1/items/", json={
        'name': "ItemN",
        'due_date': '2019-12-04T12:13',
        'finished': False,

    })
    assert response.status_code == 200
    assert response.json() == {
        'due_date': '2019-12-04T12:13:00',
        'finished': False,
        'id': 'rererer',
        'name': 'ItemN'
    }


def test_update_item(mongodb_):
    response = client.put("/lists/$list1/items/$item1", json={
        'name': "ItemN",
        'due_date': '2019-12-04T12:13',
        'finished': False,
    })
    assert response.status_code == 200
    assert response.json() == {
        'due_date': '2019-12-04T12:13:00',
        'finished': False,
        'id': '$item1',
        'name': 'ItemN'
    }


def test_delete_item(mongodb_):
    response = client.delete("/lists/$list1/items/$item1")
    assert response.status_code == 200
    assert mongodb_.items.find_one({'_id': {'$eq': '$item1'}}) is None
