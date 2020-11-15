from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import LoginForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage



def login_user(request):
    print('********')
    title = "Login"
    message = ""

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('iscae_emploi/index/')
        else:
            message = "il ya une erreur du nom ou du mots de passe"

    return render(request, 'user/login.html',locals())


def logout_user(request):
    logout(request)
    return redirect('/')


