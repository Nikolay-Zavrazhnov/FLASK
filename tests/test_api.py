import datetime

import requests

from tests.config import API_URL


def test_request_work():
    response = requests.get('http://127.0.0.1:5000')
    assert response.status_code == 404


def test_get_owner(create_owner):
    new_owner = create_owner
    response = requests.get(f"{API_URL}/users/{new_owner['id']}")
    assert response.status_code == 200
    response_data = response.json()
    assert response_data['name'] == new_owner['name']


def test_get_owner_not_exist():
    response = requests.get(f"{API_URL}/users/5555")
    assert response.status_code == 404


def test_create_owner():
    response = requests.post(f"{API_URL}/users/", json={'name': 'ANY_USER_NAME'})
    assert response.status_code == 200
    json_data = response.json()
    print(json_data)
    assert 'id' in json_data
    assert json_data['name'] == 'ANY_USER_NAME'


def test_get_adv(create_adv):
    new_adv = create_adv
    response = requests.get(f"{API_URL}/advertisements/{new_adv['id']}")
    assert response.status_code == 200
    response_data = response.json()
    assert response_data['title'] == new_adv['title']


def test_create_adv():
    create_date = datetime.datetime.now()
    response = requests.post(f"{API_URL}/advertisements/",
                             json={'title': 'new_title_adv',
                                   'text': 'new_text_advertisement',
                                   'published_at': f"{create_date}", 'user_id': 1})
    assert response.status_code == 200


def test_get_adv_not_exist():
    response = requests.get(f"{API_URL}/test_get_adv/5555")
    assert response.status_code == 404


def test_patch_adv(create_adv):
    date_new = datetime.datetime.now()
    print(date_new)
    response = requests.patch(f"{API_URL}/advertisements/{create_adv['id']}", json={
        'title': 'new_title_advertisements',
        'text': 'some_text_advertisements',
        'published_at': f'{date_new}',
        'user_id': 1,
    })
    print(response.json())
    assert response.status_code == 200


def test_delete_adv(create_adv):
    response = requests.delete(f"{API_URL}/advertisements/{create_adv['id']}")
    assert response.status_code == 200
