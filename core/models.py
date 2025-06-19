from django.db import models
from accounts.models import User
from autoslug import AutoSlugField
import uuid

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Course(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='name', unique=True)
    category = models.ForeignKey(Category, related_name="courses", on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Module(models.Model):
    name = models.CharField(max_length=255)
    course = models.ForeignKey(Course, related_name='modules', on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.course.name}"

class Lesson(models.Model):
    name = models.CharField()
    content = models.TextField()
    module = models.ForeignKey(Module, related_name='lessons', on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.name}"

class Enrollment(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='enrolled')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Progress(models.Model):
    user = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='progreses')
    completed_at = models.DateTimeField(auto_now_add=True)

class Review(models.Model):
    user = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name='reviews', on_delete=models.CASCADE)
    stars = models.PositiveIntegerField(default=1)
    messege = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Payment(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('success', 'Success'),
        ('failed', 'Failed')
    )
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='payments', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name='payments', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, default='pending', choices=STATUS_CHOICES)
    provider = models.CharField(max_length=20, default='stripe')
    transaction_id = models.UUIDField(default=uuid.uuid4,unique=True, editable=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Invoice(models.Model):
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, related_name='invoices')
    invoice_number = models.IntegerField(default=1)
    generated_at = models.DateTimeField(auto_now_add=True)
    billing_email = models.EmailField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    final_amount = models.DecimalField(max_digits=10, decimal_places=2)

class Coupon(models.Model):
    code = models.CharField(max_length=20)
    limit = models.PositiveIntegerField()
    used = models.PositiveIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
