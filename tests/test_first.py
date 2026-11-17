import pytest
from config import BASE_URL

@pytest.mark.parametrize(
    "user_id,status",
    [
    (1,200),
    (2,200),
    (10,200),
    (9999,404)
    ]
)
def test_get_user(api_client,user_id,status):
    api_response =api_client.get(f"/users/{user_id}")

    # print(api_response.json())
    assert api_response.status_code == status

    if api_response.status_code == 200:                
        header = api_response.headers
        assert header['Content-Type'].split(";")[0].strip().lower() == "application/json"
        dict_data = api_response.json()
        assert dict_data['id'] == user_id
        assert dict_data['email']
        assert isinstance(dict_data['email'],str)
        assert '@' in dict_data['email']
        assert isinstance(dict_data['address'],dict)
        assert 'city' and 'zipcode' in dict_data['address']
        print(dict_data['address'])


def test_create_post(api_client):
    payload = {
        "title": "API Automation",
        "body": "Learning Python Requests",
        "userId": 1
    }
    api_post_response = api_client.post("/posts",payload)
    # print(api_post_response.headers)
    print(api_post_response.json())

def test_update_post(api_client):
    payload = {
        "id": 1,
        "title": "Updated API Automation",
        "body": "Learning PUT requests",
        "userId": 1
    }

    print("")
    response_get = api_client.get("/posts/1")
    print(response_get.json())

    response= api_client.put("/posts/1",payload)
    print(response.json())

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]