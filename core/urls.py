from django.urls import path
from django.http import HttpResponse
from . import views

app_name = "core"

urlpatterns = [

    # Courses and contents
    path('courses/', views.CourseListView.as_view()),
    path('courses/<int:pk>/', views.CourseDetailView.as_view()),

    path('courses/<int:course_id>/modules/', views.ModuleListCreateAPIView.as_view()),
    path('courses/modules/<int:pk>/', views.ModuleDetailAPIView.as_view()),





    path('payments/create/', views.PaymentCreateView.as_view()),
]

