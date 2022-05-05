import pytest

from fastapi.testclient import TestClient
from models.job import Job, JobModel
from app import app


@pytest.fixture
def job():
    job = Job(title="Engenheiro de dados pleno", description="Vaga de engenheiro de dados pleno",
              employer="Toptal", location="New York, USA")
    return job


@pytest.fixture
def database_mock(monkeypatch):
    monkeypatch.setenv("DATABASE_URI", "sqlite:///:memory:")


@pytest.fixture
def client():
    return TestClient(app)
