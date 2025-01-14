from account.views import profile_view
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed

def test_profile_view(client):
    response = client.get(reverse('account:profile'))
    assert response.status_code == 200
    assertTemplateUsed(response, 'account/profile.html')