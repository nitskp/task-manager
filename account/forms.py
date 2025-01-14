from django import forms

class ProfileForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='First Name')
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='Last Name')
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-email'}), label='Email')
    photo = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control'}), label='Photo')
