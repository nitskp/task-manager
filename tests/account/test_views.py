from account.views import profile_view
from account.forms import ProfileForm
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed, assertFormError, assertContains

def test_profile_view(client):
    response = client.get(reverse('account:profile'))
    assert response.status_code == 200
    assertTemplateUsed(response, 'account/profile.html')
    # Contains profileForm test
    assert isinstance(response.context['profile_form'], ProfileForm)