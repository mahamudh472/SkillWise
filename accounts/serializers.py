from rest_framework import serializers
from .models import User, UserProfile
from core.serializers import CourseSerializer

class UserSerializer(serializers.ModelSerializer):
    enrolled_courses = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'enrolled_courses']
    def get_enrolled_courses(self, obj):
        enrolments = obj.enrolled.select_related('course')
        return CourseSerializer([e.course for e in enrolments], many=True).data

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = UserProfile
        fields = '__all__'
        