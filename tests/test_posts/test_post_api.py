from tests.utils.auth import auth_header


def test_create_get_post(client):
    body = {"title": "Post 1", "description": "post1 description"}
    response = client.post("/posts", json=body, headers=auth_header)

    assert response.status_code == 201
    response_json = response.json

    assert response_json["id"]
    assert response_json["title"] == body["title"]
    assert response_json["description"] == body["description"]
    assert response_json["likes_count"] == 0
    assert response_json["owner"]
    assert response_json["comments"] == []
    assert response_json["likes"] == []
    assert response_json["created"]
    assert response_json["updated"]


def test_get_all_posts(client):
    response = client.get("/posts")
    assert response.status_code == 200
    response_json = response.json
    assert isinstance(response_json, list)
