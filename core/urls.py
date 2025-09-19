from django.urls import path
from django.http import HttpResponse
from . import views

app_name = "core"

urlpatterns = [

    # Courses and contents
    path('courses/', views.CourseListView.as_view()),
    path('courses/<int:pk>/', views.CourseDetailView.as_view()),

    path('courses/<int:course_id>/modules/', views.ModuleListCreateAPIView.as_view()),
    path('modules/<int:pk>/', views.ModuleDetailAPIView.as_view()),

    path('modules/<int:module_id>/lessons/', views.LessonListCreateAPIView.as_view()),
    path('lessons/<int:pk>/', views.LessonDetailAPIView.as_view()),



    path('payments/create/', views.PaymentCreateView.as_view()),
    path('payments/success/', lambda request: HttpResponse("Payment Success"), name='payment-success' ),
    path('payments/cancel/', lambda request: HttpResponse("Payment Cancelled"), name='payment-cancel' ),
]

