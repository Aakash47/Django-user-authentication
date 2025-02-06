from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
# Create your views here.


@login_required(login_url="/login/")
def home(request):
    return render(request, 'dashboard.html',)


@login_required(login_url="/login/")
def profile(request):
    user=request.user
    context={
        'user':user,
    }
    return render(request, 'profile.html', context)


def register(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, "Account has been created for " + user)
                return redirect('login')

        context = {
            'form': form,
        }
        return render(request, 'register.html', context)


def loginpage(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.info(request, "Username or Password is incorrect")

    return render(request, 'login.html')


@login_required(login_url="/login/")
def logoutuser(request):
    logout(request)
    return redirect('login')


@login_required(login_url="/login/")
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            
            messages.success(request, 'Your password was successfully updated!')
            logout(request)
            return redirect('login')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    context={
        'form': form,
    }
    return render(request, 'change_password.html', context)