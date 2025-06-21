from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView, Response
from .models import User, UserProfile
from .serializers import ProfileSerializer
# Create your views here.
def register(request):
    return HttpResponse("Register page")

def login(request):
    return HttpResponse('Login page')

class ProfileView(APIView):
    def get(self, request):
        profile = UserProfile.objects.get(user=request.user)
        return Response(ProfileSerializer(profile).data)