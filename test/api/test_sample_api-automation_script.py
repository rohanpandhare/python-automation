import requests
from data.user_data import user_data

base_url = 'https://reqres.in'
list_users_endpoint = '/api/users?page=2'
create_user_endpoint = '/api/users'

user_json_data = {
    "name": "morpheus",
    "job": "leader"
}


def test_get_request():
    """test case to make and assert response of GET call"""
    response = requests.get(url=base_url + list_users_endpoint)
    assert response.status_code == 200


def test_post_request():
    """test case to make and assert response of POST call
       using locally available json data
    """
    response = requests.post(url=base_url+create_user_endpoint, json=user_json_data)
    assert response.status_code == 201
    print(response.text)


def test_post_request_2():
    """test case to make and assert response of POST call
       using json data from another file
    """
    response = requests.post(url=base_url+create_user_endpoint, json=user_data)
    assert response.status_code == 201
    print(response.json())
