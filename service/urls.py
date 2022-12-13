from django.template.defaulttags import url
from django.urls import path
from django.conf import settings
from .views import LoginUser, RegisterUser, DataUser, logout_user

from .views import *

urlpatterns = [
    path('', MainView.as_view(), name='main_page'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name="logout"),
    path('reg/', RegisterUser.as_view(), name='reg'),
    path('client/<int:pk>/', DataUser.as_view(), name='client'),
]