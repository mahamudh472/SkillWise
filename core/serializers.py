from rest_framework import serializers
from .models import (
    Category, Course, Coupon,Enrollment, Invoice, Lesson, Module, Payment, Progress, Review
)
class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'

class ModuleSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True)
    class Meta:
        model = Module
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    modules_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Course
        fields = ['author', 'name', 'price', 'category', 'modules_count']
    
    def get_modules_count(self, obj):
        return obj.modules.count()
    def get_category(self, obj):
        return obj.category.name
