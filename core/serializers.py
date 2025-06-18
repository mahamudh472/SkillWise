from rest_framework import serializers
from .models import (
    Category, Course, Coupon,Enrollment, Invoice, Lesson, Module, Payment, Progress, Review
)

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'