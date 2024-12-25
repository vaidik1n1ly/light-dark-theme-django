from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.shortcuts import render
from .models import Setting
from .serializers import UserSerailizer

class ThemeSettingView(APIView):
    def get(self, request, format=None):
        user = User.objects.first()
        
        setting, created = Setting.objects.get_or_create(user=user, name='theme', defaults={'value': 'light'})
        serializer = UserSerailizer(setting)
        
        return Response(serializer.data)


    def post(self, request, format=None):
        user = User.objects.first()
        
        setting = Setting.objects.get(user=user, name='theme')
        serializer = UserSerailizer(setting, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

def index(request):
    return render(request, 'base/index.html')