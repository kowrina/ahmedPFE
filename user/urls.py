from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.static import static
from django.conf import settings
app_name='user'

urlpatterns = [

    # path('login/', LoginView.as_view(template_name='user/login.html'), name='login'),
    path('', views.login_user, name=''),
    # path('logout/', LogoutView.as_view(template_name='user/logout.html'), name='logout'),
    path('logout/', views.logout_user, name='logout')
    ,]





