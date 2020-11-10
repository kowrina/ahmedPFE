from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage



def login_user(request):
    print('********')
    title = "Login"

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('iscae_emploi/index/')
        else:
            messages.warning(
                request, 'هناك خطأ في اسم المستخدم أو كلمة المرور.')

    return render(request, 'user/login.html',locals())


def logout_user(request):
    logout(request)
    return render(request, 'user/logout.html', {
        'title': 'تسجيل الخروج'
    })



