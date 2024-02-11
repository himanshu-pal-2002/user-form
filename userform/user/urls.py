from django.urls import path
from .views import *


urlpatterns=[
    path('',Home,name='Home'),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]