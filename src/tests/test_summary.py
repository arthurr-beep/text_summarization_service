import json

import pytest


def test_create_summary(test_app_with_db):
    response = test_app_with_db.post("/summary/", data=json.dumps({"url": "https://testurl.com"}))

    assert response.status_code == 201
    assert response.json()["url"] == "https://testurl.com"

def test_create_summary_invalid_json(test_app):
    response = test_app.post("/summary/", data=json.dumps({}))
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "loc": ["body", "url"],
                "msg": "field required",
                "type": "value_error.missing"
            }
        ]
    }


def test_read_summary(test_app_with_db):
    response = test_app_with_db.post("/summary/", data=json.dumps({"url": "https://foo.bar"}))
    summary_id = response.json()["id"]

    response = test_app_with_db.get(f"/summary/{summary_id}/")
    assert response.status_code == 200

    response_dict = response.json()
    assert response_dict["id"] == summary_id
    assert response_dict["url"] == "https://foo.bar"
    assert response_dict["summary"]
    assert response_dict["created_at"]

def test_read_summary_incorrect_id(test_app_with_db):
    response = test_app_with_db.get("/summary/999/")
    assert response.status_code == 404
    assert response.json()["detail"] == "Summary not found"

def test_read_all_summaries(test_app_with_db):
    response = test_app_with_db.post("/summary/", data=json.dumps({"url": "https://foo.bar"}))
    summary_id = response.json()["id"]

    response = test_app_with_db.get("/summary/")
    assert response.status_code == 200

    response_list = response.json()
    assert len(list(filter(lambda d: d["id"] == summary_id, response_list))) == 1
