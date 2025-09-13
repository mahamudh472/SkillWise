from django.urls import path
from django.http import HttpResponse
from . import views

app_name = "core"

urlpatterns = [
    path('courses/', views.CourseListView.as_view()),
    path('courses/<int:pk>/', views.CourseDetailView.as_view()),
    path('payments/create/', views.PaymentCreateView.as_view()),
]

