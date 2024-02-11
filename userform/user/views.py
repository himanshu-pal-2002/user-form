from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from django.conf import settings
from .serializers import UserFormSerializer
from django.shortcuts import render
# from .forms import *
from rest_framework.generics import ListCreateAPIView
from .models import *

class UserListCreate(ListCreateAPIView):
    queryset = UserRegistration.objects.all()
    serializer_class = UserFormSerializer



class UserRegistrationView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserFormSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            send_mail(
                'Registration Successful',
                f'Hello {user.name}, your registration was successful. Your details are Name: {user.name}, Date of Birth: {user.date_of_birth}, Email: {user.email}, and Phone Number: {user.phone_number}.',
                'palhimanshu206246@gmail.com',
                [user.email],
                fail_silently=False
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



