from iebank_api import app
import pytest


def test_skull_route(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/skull' page is requested (GET)
    THEN check the response is valid
    """
    response = testing_client.get('/skull')
    assert response.status_code == 200
    assert 'BACKEND SKULL' in response.data.decode('utf-8')

def test_get_accounts(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/accounts' page is requested (GET)
    THEN check the response is valid
    """
    response = testing_client.get('/accounts')
    assert response.status_code == 200

def test_dummy_wrong_path():
    """
    GIVEN a Flask application
    WHEN the '/wrong_path' page is requested (GET)
    THEN check the response is valid
    """
    with app.test_client() as client:
        response = client.get('/wrong_path')
        assert response.status_code == 404

def test_create_account(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/accounts' page is posted to (POST)
    THEN check the response is valid
    """
    response = testing_client.post('/accounts', json={'name': 'John Doe', 'currency': '€', 'country': 'ESP'})
    assert response.status_code == 200

def test_account_country(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/accounts' page is posted to (POST)
    THEN check the response is valid
    """
    uuid = "d88d6966-7384-4e86-9a1f-40f51ee2cb83"
    response = testing_client.post('/accounts', json={'name': uuid, 'currency': '€', 'country': 'ESP'})
    assert response.status_code == 200
    response = testing_client.get('/accounts')
    assert response.status_code == 200
    account = [account for account in response.json['accounts'] if account['name'] == uuid]
    assert len(account) == 1
    account = account[0]
    assert account['country'] == 'ESP'

def test_add_and_get_account(testing_client):
    """
    WHEN the '/accounts' page is posted to (POST)
    THEN check the response is valid
    AND the '/accounts/<id>' page is requested (GET)
    THEN check the response is valid
    """
    uuid = "d88d6966-7384-4e86-9a1f-40f51ee2cb83"
    response = testing_client.post('/accounts', json={'name': uuid, 'currency': '€', 'country': 'ESP'})
    assert response.status_code == 200
    account_id = response.json['id']
    response = testing_client.get(f'/accounts/{account_id}')
    assert response.status_code == 200
    account = response.json
    assert account['name'] == uuid
    assert account['country'] == 'ESP'
    assert account['id'] == account_id
    assert account['currency'] == '€'

def test_update_account_name(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/accounts' page is posted to (POST)
    THEN check the response is valid
    AND the '/accounts/<id>' page is updated (PUT)
    THEN check the response is valid
    """
    uuid = "d88d6966-7384-4e86-9a1f-40f51ee2cb83"
    response = testing_client.post('/accounts', json={'name': uuid, 'currency': '€', 'country': 'ESP'})
    assert response.status_code == 200
    account_id = response.json['id']
    response = testing_client.put(f'/accounts/{account_id}', json={'name': 'Jane Doe'})
    assert response.status_code == 200
    response = testing_client.get(f'/accounts/{account_id}')
    assert response.status_code == 200
    account = response.json
    assert account['name'] == 'Jane Doe'
    assert account['country'] == 'ESP'
    assert account['id'] == account_id
    assert account['currency'] == '€'


def test_delete_account(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/accounts' page is posted to (POST)
    THEN check the response is valid
    AND the '/accounts/<id>' page is deleted (DELETE)
    THEN check the response is valid
    """
    uuid = "d88d6966-7384-4e86-9a1f-40f51ee2cb83"
    response = testing_client.post('/accounts', json={'name': uuid, 'currency': '€', 'country': 'ESP'})
    assert response.status_code == 200
    account_id = response.json['id']
    response = testing_client.delete(f'/accounts/{account_id}')
    assert response.status_code == 200
    response = testing_client.get(f'/accounts/{account_id}')
    assert response.status_code == 404
