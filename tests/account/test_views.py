from account.views import profile_view
from account.forms import ProfileForm
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed, assertFormError, assertContains
from django.core.files.uploadedfile import SimpleUploadedFile

def test_profile_view_get(client):
    response = client.get(reverse('account:profile'))
    assert response.status_code == 200
    assertTemplateUsed(response, 'account/profile.html')
    # Contains profileForm test
    assert isinstance(response.context['profile_form'], ProfileForm)

def test_profile_view_post(client):
    photo = SimpleUploadedFile(name='HxH-fanfic-icon.jpeg', 
                            content=b'This is a dummy image file content',
                            content_type='image/jpeg')
    
    response = client.post(reverse('account:profile'), data = {
        'csrfmiddlewaretoken': 'DTjupuJy2AXn3r6IhQAGZGYzAQQtwMj6b829G2w7P0pqw1mZk5sfAPr1zT9hBehB',
        'first_name': 'dsdssdd',
        'last_name': 'ds',
        'email': 'sds@gmail.com',
        'photo': photo,
        'role': 'manager'
    })

     # Initialize the ProfileForm with the same data used in the POST request
    form_data = {
        'first_name': 'dsdssdd',
        'last_name': 'ds',
        'email': 'sds@gmail.com',
        'role': 'manager'
    }

    profile_form = ProfileForm(data=form_data, files={'photo': photo})
    assert response.status_code == 200
    assert 'Profile updated' == response.content.decode()
    assert profile_form.is_valid()