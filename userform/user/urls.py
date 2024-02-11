from django.urls import path
from .views import UserFormView


urlpatterns=[
    path('register/', UserFormView.as_view(), name='UserFormView'),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]