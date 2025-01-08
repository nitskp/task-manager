from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseBadRequest, HttpResponseServerError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.urls import reverse

# Create your views here.
def registration_view(request:HttpRequest):
    if request.method == 'POST':
        registration_form = UserCreationForm(request.POST)
        if registration_form.is_valid():
            username = registration_form.cleaned_data['username']
            password = registration_form.cleaned_data['password1']
            try:
                user = User.objects.create(username=username,password=password)
            except KeyError:
                return HttpResponseBadRequest('Username already registered.')
            except Exception as e:
                print(f'Following exception occured while creating user : {e}')
                return HttpResponseServerError('Some error occured.')
            else:
                return HttpResponse(f'User with username : {user.username} created')
    else:
        registration_form = UserCreationForm()
        return render(request, 'account/registration.html', {
            'form': registration_form
        })

def login_view(request:HttpRequest):
    if request.method == 'POST':
        auth_form = AuthenticationForm(request.POST)
        if auth_form.is_valid():
            username = auth_form.cleaned_data['username']
            password = auth_form.cleaned_data['password']
            user = authenticate(request=request,username=username, password=password)
            if user:
                login(request=request, user=user)
                return HttpResponse(f'User : {username} logged in')
            else:
                return HttpResponse(f'No user with {username} found.', status=404)
        else:
            return HttpResponseBadRequest('Invalid form details')
    else:
        auth_form = AuthenticationForm()
        return render(request, 'account/login.html', {
            'form': auth_form
        })
        

def logout(request:HttpRequest):
    logout(request=request)
    return reverse('account:login')