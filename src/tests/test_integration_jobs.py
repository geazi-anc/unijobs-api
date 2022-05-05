import pytest


def test_create_a_new_job(client, job):
    response = client.post('/jobs', json=job.dict())

    assert response.status_code == 201
    assert response.json() == job.dict()

