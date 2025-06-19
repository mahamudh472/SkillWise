from django.shortcuts import render
from rest_framework import generics, views, response, permissions
from .models import Course
from .serializers import CourseSerializer

class CourseListView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseDetailView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, pk):
        course = Course.objects.get(id=pk)
        serializer = CourseSerializer(course)
        return response.Response(serializer.data)