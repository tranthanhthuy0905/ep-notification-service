import pytest
from notification.tests.fixtures import outlook_url, outlook_ubject, outlook_recipient, message

@pytest.mark.django_db
def test_post_outlook_full(client):
    post_data = {
        'subject': outlook_ubject,
        'recipient': outlook_recipient,
        'message': message
    }
    response = client.post(outlook_url, post_data)
    assert response.status_code == 201

@pytest.mark.django_db
def test_post_outlook_no_subject(client):
    post_data = {
        'recipient': outlook_recipient,
        'message': message
    }
    response = client.post(outlook_url, post_data)
    assert response.status_code == 201

@pytest.mark.django_db
def test_post_outlook_no_recipient(client):
    post_data = {
        'subject': outlook_ubject,
        'message': message
    }
    response = client.post(outlook_url, post_data)
    assert response.status_code == 400

@pytest.mark.django_db
def test_post_outlook_nothing(client):
    post_data = {
        'message': message
    }
    response = client.post(outlook_url, post_data)
    assert response.status_code == 400