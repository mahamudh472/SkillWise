from django.urls import path
from django.http import HttpResponse
from . import views

app_name = "core"

urlpatterns = [
    path('courses/', views.CourseList.as_view())
]

