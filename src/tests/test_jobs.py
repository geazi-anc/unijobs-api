import os
import pytest

from fastapi.testclient import TestClient

from app import app


##### ARRANGE #####
@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def default_job():
    job = {
        'title': 'Fullstack Engineer',
        'description': 'Venha fazer parte de nosso time!',
        'employer': 'Google Brasil',
        'location': 'SP, Brasil',
    }

    return job


@pytest.fixture
def default_saved_job(default_job):
    saved_job = default_job.copy()
    saved_job['id'] = 1

    return saved_job


@pytest.fixture
def default_job_url(default_saved_job):
    id = default_saved_job['id']
    url = f'/jobs/{id}'

    return url

##### TESTS #####


def test_post_a_new_job(client, default_job, default_saved_job):
    response = client.post('/jobs', json=default_job)

    assert response.status_code == 201
    assert response.json() == default_saved_job


def test_get_all_jobs(client):
    response = client.get('/jobs')

    assert response.status_code == 200
    assert len(response.json()) == 1


def test_get_job_by_id(client, default_saved_job, default_job_url):
    response = client.get(default_job_url)

    assert response.status_code == 200
    assert response.json() == default_saved_job


def test_delete_job_without_apikey(client, default_saved_job, default_job_url):
    headers = {
        'X-Apikey': '54321'
    }

    response = client.delete(default_job_url, headers=headers)

    assert response.status_code == 401
    assert response.json() == {
        'detail': 'You do not have permission to delete a job. Please add a valid API Key in x-apikey header.'}


def test_delete_job_with_apikey(client, default_saved_job, default_job_url):
    headers = {
        'X-Apikey': os.environ['API_KEY']
    }

    response = client.delete(default_job_url, headers=headers)

    assert response.status_code == 200
    assert response.json() == default_saved_job
