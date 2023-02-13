from django.urls import path
from . import views

urlpatterns = [
    path('profile/<str:pk>', views.profile, name = 'profile'),
    path('account', views.account, name = 'account'),
    path('registration', views.registration, name = 'registration'),
    path('login', views.signin, name = 'signin'),
    path('logout', views.signout, name = 'signout'),
    path('profile-update', views.updateProfile, name = 'profile-update')

]