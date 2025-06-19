from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView
app_name = "accounts"

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login')
]

