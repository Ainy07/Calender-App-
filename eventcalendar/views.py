from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from calendarapp.forms import SigninForm

def signin(request):
    forms = SigninForm()
    if request.method == 'POST':
        forms = SigninForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('calendarapp:calendar')
    context = {'form': forms}
    return render(request, 'signin.html', context)


def user_logout(request):
    logout(request)
    return redirect('signin')