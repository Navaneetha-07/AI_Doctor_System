from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .forms import RegisterForm


# Home Page
def home(request):
    return render(request, 'home.html')


# Register
def register(request):

    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            user.set_password(
                form.cleaned_data['password']
            )

            user.save()

            return redirect('login')
        else:
            print(form.errors)
            

    else:
        
        

        form = RegisterForm()

    return render(
        request,
        'accounts/register.html',
        {'form': form}
    )


# Login
def user_login(request):

    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect('dashboard')

        else:

            return render(
                request,
                'accounts/login.html',
                {'error': 'Invalid Username or Password'}
            )

    return render(
        request,
        'accounts/login.html'
    )


# Dashboard
def dashboard(request):
    return render(
        request,
        'accounts/dashboard.html'
    )