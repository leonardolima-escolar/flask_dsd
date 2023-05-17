import requests
from werkzeug.wrappers import response

api_url = 'http://127.0.0.1:8090/countries'


def get():
    response = requests.get(api_url)
    print(response.json())


def insert():
    country = {"country_name": "d", "capital": "e"}
    response = requests.post(api_url, json=country)
    print(response.json())


def get_by_id():
    url_id = f'{api_url}/7'
    response = requests.get(url_id)
    print(response.json())


def edit_by_id():
    url_id = f'{api_url}/7'
    country = {"country_name": "b", "capital": "c"}
    response = requests.put(url_id, json=country)
    print(response.json())


def delete_by_id():
    url_id = f'{api_url}/7'
    response = requests.delete(url_id)
    print(response.json())


# get_by_id()
# delete_by_id()
# get_by_id()
# get_by_id()
# edit_by_id()
# get_by_id()
# get()
# insert()
get()
