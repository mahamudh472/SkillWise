from django.shortcuts import render
from rest_framework import generics, views, response, permissions
from .models import Course, Enrollment
from .serializers import CourseSerializer, CourseDetailsSerializer, TempCourseSerializer
from accounts.permissions import IsInstructor
from rest_framework.exceptions import PermissionDenied, NotFound
from django.db.models.functions import Upper

class CourseListView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseDetailView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        try:
            return Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            raise NotFound('Course not found')

    def get(self, request, pk):
        course = self.get_object(pk=pk)
        user = request.user
        if user.role.lower() == 'instructor' and user==course.author:
            pass
        elif user in Enrollment.objects.filter(student=user, course=course):
            pass
        else:
            raise PermissionDenied("You do not have access to this course.")

        serializer = CourseDetailsSerializer(course)
        return response.Response(serializer.data)

class TempCourseAPIView(views.APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):

        courses = Course.objects.all()
        serializer = TempCourseSerializer(courses, many=True)
        from pprint import pprint
        temp_data = Course.objects.values_list('name', flat=True)
        pprint(temp_data)
        
        return response.Response(serializer.data)
