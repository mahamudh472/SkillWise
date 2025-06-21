from django.db import models
from django.contrib.auth.models import AbstractUser, Group

class User(AbstractUser):
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('instructor', 'Instructor'),
        ('admin', 'Admin')
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='student')

    def save(self, *args, **kwargs):
        is_new = self.pk is None
        super().save(*args, **kwargs)

        if is_new:
            UserProfile.objects.create(user=self, bio='default')

            try:
                group_name = self.role.capitalize()
                group = Group.objects.get(name=group_name)
                self.groups.add(group)
            except Group.DoesNotExist:
                print(f"[WARNING] Group '{self.role}' does not exist.")

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatar/', blank=True, null=True)
    bio = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Userprofile of {self.user.username}"
    