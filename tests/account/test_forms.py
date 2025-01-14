from account.forms import ProfileForm
from django import forms

def test_profile_form_fields_and_types():
    form = ProfileForm()
    form_fields = form.fields.keys()
    expected_fields = ['first_name', 'last_name', 'photo', 'email' ]    
    assert set(form_fields) == set(expected_fields)
    assert isinstance(form.fields['first_name'], forms.CharField)
    assert isinstance(form.fields['last_name'], forms.CharField)
    assert isinstance(form.fields['photo'], forms.FileField)
    assert isinstance(form.fields['email'], forms.EmailField)