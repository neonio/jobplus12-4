import os
import pytest
from manage import app
from jobplus.models import db, User


@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    yield client


def test_index(client):
    rv = client.get('/')
    assert rv.status == '200 OK'
