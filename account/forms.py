from django import forms

class ProfileForm(forms.Form):
    first_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}), label='First Name')
    last_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}), label='Last Name')
    email = forms.EmailField(max_length=255, widget=forms.EmailInput(attrs={'class': 'form-email'}), label='Email')
    photo = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control'}), label='Photo')
