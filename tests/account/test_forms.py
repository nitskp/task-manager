from account.forms import ProfileForm
from django import forms
from account.utils import ROLES

def test_profile_form_fields_and_types():
    form = ProfileForm()
    form_fields = form.fields.keys()
    expected_fields = ['first_name', 'last_name', 'photo', 'email', 'role' ]    
    assert set(form_fields) == set(expected_fields)
    assert isinstance(form.fields['first_name'], forms.CharField)
    assert isinstance(form.fields['last_name'], forms.CharField)
    assert isinstance(form.fields['photo'], forms.FileField)
    assert isinstance(form.fields['email'], forms.EmailField)
    


def test_profile_form_field_validation():
    profile_form = ProfileForm()
    assert profile_form.fields['first_name'].max_length == 255
    assert profile_form.fields['last_name'].max_length == 255
    assert profile_form.fields['email'].max_length == 255
    assert profile_form.fields['role'].choices == ROLES
   