from django.shortcuts import render
from rest_framework import  status
from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView
)
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Course, Enrollment, Module, Lesson
from .serializers import (
    CourseSerializer, 
    CourseDetailsSerializer, 
    ModuleSerializer, LessonSerializer
    )
from accounts.permissions import IsInstructor
from rest_framework.exceptions import PermissionDenied, NotFound
from django.db.models.functions import Upper

class CourseListView(ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseDetailView(APIView):
    permission_classes = [IsAuthenticated]

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
        elif Enrollment.objects.filter(student=user, course=course).exists():
            pass
        else:
            raise PermissionDenied("You do not have access to this course.")

        serializer = CourseDetailsSerializer(course)
        return Response(serializer.data)

class CourseUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    permission_classes = [IsInstructor]
    serializer_class = CourseSerializer

class ModuleListCreateAPIView(ListCreateAPIView):
    serializer_class = ModuleSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):       
        return Module.objects.filter(course__id=self.kwargs['course_id']) 
    

class ModuleDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        module = Module.objects.filter(pk=pk)
        if module.exists():
            module = module.first()
        else:
            raise NotFound("Module Not Found")
        course = module.course
        if not Enrollment.objects.filter(course=course, student=request.user).exists():
            raise PermissionDenied("You don't have access to this course.")
        serializer = ModuleSerializer(module)
        return Response(serializer.data)

class LessonListCreateAPIView(ListCreateAPIView):   
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):       
        return Lesson.objects.filter(module__id=self.kwargs['module_id'])


class LessonDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        lesson = Lesson.objects.filter(pk=pk)
        if lesson.exists():
            lesson = lesson.first()
        else:
            raise NotFound("Lesson Not Found")
        module = lesson.module
        course = module.course
        if not Enrollment.objects.filter(course=course, student=request.user).exists():
            raise PermissionDenied("You don't have access to this course.")
        serializer = LessonSerializer(lesson)
        return Response(serializer.data)

class PaymentCreateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        course_id = request.data.get("course_id", None)
        course = Course.objects.filter(id=course_id)
        if course.exists():
            course = course.first()
            price = course.price
            Enrollment.objects.create(
                student=request.user,
                course=course
            )
        else:
            return Response({
                "Error": "Course not found"
            }, status=status.HTTP_404_NOT_FOUND)
        print(course.name, course.price)

        checkout_url = True

        return Response({
            "checkout_url": checkout_url,
            # "course": course
        })
