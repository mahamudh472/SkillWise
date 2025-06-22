from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView, Response
from .models import User, UserProfile
from .serializers import ProfileSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
# Create your views here.

class RegisterView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        password = request.data.get('password')
        role = request.data.get('role')

        if User.objects.filter(email=email):
            return Response({'error': 'Email already exists'})
        if User.objects.filter(username=username):
            return Response({'error': 'Username already exists.'})
        user = User.objects.create_user(
            email=email,
            username=username,
            password=password,
            role=role,
            first_name=first_name,
            last_name=last_name
        )
        return Response({'success': f'Account successfully created for: {username}'})


class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        profile = UserProfile.objects.get(user=request.user)
        return Response(ProfileSerializer(profile).data)

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        try:
            refresh_token = request.data['refresh']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({'message': 'logout successful.'})
        except KeyError:
            return Response({'error': 'refresh token is required.'})
        except TokenError:
            return Response({'error': 'invalid or expired token'})

