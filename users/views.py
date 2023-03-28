from django.shortcuts import render
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView
from .serializers import UserSerializer
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from django.shortcuts import get_object_or_404
from .serializers import UserSerializer

class GoogleLogin(SocialLoginView): # if you want to use Implicit Grant, use this
    adapter_class = GoogleOAuth2Adapter

class UserDetail(APIView):
    
    def get(self, request):
        user_serialzer = UserSerializer(request.user)
        return Response(user_serialzer.data)
    
class MyProfile(APIView):
    
    def get(self, request, *args, **kwargs):
        user = get_object_or_404(User, pk=kwargs['pk'])
        profile_serializer = UserSerializer(user)
        return Response(profile_serializer.data, status=status.HTTP_200_OK)