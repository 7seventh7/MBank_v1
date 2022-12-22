import pytest
import requests

class TestUserAuth:
    def test_response_status(self):
        response = requests.get('http://127.0.0.1:8000/api/customerlist')
        assert response.status_code == 200, 'Some issues, could not connect!'

    def test_create_user(self):
        response = requests.get('http://127.0.0.1:8000/api/customerlist/api/v1/sdrf-auth/')


