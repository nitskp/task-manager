from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseBadRequest, HttpResponseServerError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.urls import reverse
from .forms import ProfileForm

# Create your views here.
def registration_view(request:HttpRequest):
    if request.method == 'POST':
        registration_form = UserCreationForm(request.POST)
        valid_data = request.POST
        print(f'Valid data : {valid_data}')
        if registration_form.is_valid():           
            # TODO: Need to add tests for this. Also put this in try except
            try:
                user = registration_form.save()
            except KeyError:
                return HttpResponseBadRequest('Username already registered.')
            except Exception as e:
                print(f'Following exception occured while creating user : {e}')
                return HttpResponseServerError('Some error occured.')
            else:
                return HttpResponse(f'User with username : {user.username} created')
        else:
            print(registration_form.errors)
            return HttpResponseBadRequest('Invalid form details')
    else:
        registration_form = UserCreationForm()
        return render(request, 'account/registration.html', {
            'form': registration_form
        })

def login_view(request:HttpRequest):
    if request.method == 'POST':
        auth_form = AuthenticationForm(data=request.POST)
        # Need to check if the error is due to not directly saving the form as now user's password is being saved correctly.
        if auth_form.is_valid():
            username = auth_form.cleaned_data['username']
            password = auth_form.cleaned_data['password']
            user = authenticate(request=request,username=username, password=password)
            if user is not None:
                login(request=request, user=user)
                return HttpResponse(f'User : {username} logged in')
            else:
                return HttpResponse(f'No user with {username} found.', status=404)
        else:
            print(auth_form.errors)
            return HttpResponseBadRequest('Invalid form details')
    else:
        auth_form = AuthenticationForm()
        return render(request, 'account/login.html', {
            'form': auth_form
        })
        

def logout_view(request:HttpRequest):
    try:
        logout(request)
    except Exception as e:
        raise ValueError(f'Exception occured while logging out : {e}')
    else:
        print(f'User logged out')
    return reverse('account:login')

def profile_view(request:HttpRequest):
    profile_form = ProfileForm()
    context = {
        'profile_form': profile_form
    }
    return render(request, 'account/profile.html', context)