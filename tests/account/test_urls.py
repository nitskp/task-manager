# import pytest
from django.urls import resolve
from account.views import profile_view

def test_profile_url_exits(client):
    response = client.get('/account/profile/')
    assert response.status_code == 200

def test_profile_url_resolves_correct_view():
    resolver = resolve('/account/profile/')
    assert resolver.func == profile_view