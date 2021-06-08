from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SignUpForm
# from ebook.models import EBooksModel
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm



def sign_up(request):
    if request.method == "POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request, 'Account Created Successfully !!')
            fm.save()
    else:
        fm = SignUpForm()
    return render(request, 'registration/signup.html', {'form': fm})


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    return redirect('/')
        else:
            fm = AuthenticationForm()
        return render(request, 'registration/login.html', {'form': fm})
    else:
        return redirect('/')


# Profile
def user_profile(request, id):
    # book = EBooksModel.objects.get(pk =id)
    s_form = SignUpForm(instance=request.user)
    return render(request, 'registration/profile.html', {'name': request.user, 's_form':s_form})


def user_logout(request):
    logout(request)
    return redirect('/user_login/')


