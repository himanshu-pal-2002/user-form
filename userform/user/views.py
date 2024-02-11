from django.shortcuts import render
from rest_framework import viewsets
from .models import *

# Create views for HomePage:
def Home(request):
    return render(request,'index.html')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User_Form.objects.all()
    # serializer_class = User_FormSerializer
