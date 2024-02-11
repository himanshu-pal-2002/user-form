from django.urls import path
from .views import UserRegistrationView,UserListCreate
# from .views import *


urlpatterns=[
     path('', UserListCreate.as_view(), name='UserListCreate'),
    path('register/', UserRegistrationView.as_view(), name='UserRegistrationView'),
    
]