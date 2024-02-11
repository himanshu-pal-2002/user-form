from django.urls import path
from .views import UserRegistrationView
from .views import *


urlpatterns=[
    # path('form/',form,name='form'),
    path('register/', UserRegistrationView.as_view(), name='UserRegistrationView'),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]