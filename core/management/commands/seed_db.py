from django.core.management.base import BaseCommand, CommandError
from accounts.models import User 
from core.models import Category, Course, Module, Lesson
from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType
import faker, random
fk = faker.Faker()

class Command(BaseCommand):
    help = "populate database tables with dummy data"

    def handle(self, *args, **options):
        
        try:
            self._add_user()
        except Exception as e:
            raise CommandError(f'An error occured {e}')
        
    
    # Helper functions
    def _setup_roles(self):
        try:
            student_group, _ = Group.objects.get_or_create(name="Student")
            instructor_group, _ = Group.objects.get_or_create(name="Instructor")
            admin_group, _ = Group.objects.get_or_create(name="Admin")
            models = [Course, Module, Lesson]
            for model in models:
                ct = ContentType.objects.get_for_model(model=model)
                view_permission = Permission.objects.get(codename=f'view_{model._meta.model_name}', content_type=ct)
                add_permission = Permission.objects.get(codename=f'add_{model._meta.model_name}', content_type=ct)
                change_permission = Permission.objects.get(codename=f'change_{model._meta.model_name}', content_type=ct)
                delete_permission = Permission.objects.get(codename=f'delete_{model._meta.model_name}', content_type=ct)

                student_group.permissions.add(view_permission)
                instructor_group.permissions.add(view_permission, add_permission, change_permission)
                admin_group.permissions.add(view_permission, add_permission, change_permission, delete_permission)


        except Exception as e:
            self.stdout.write(e)

    def _add_user(self):
        try:
            user = User.objects.create_user(
                username=fk.user_name(),
                email=fk.email(),
                first_name=fk.first_name(),
                last_name=fk.last_name(),
                password="1234",
                role='instructor'
            )
            user.save()
            self.stdout.write(f"User created with username: {user.username}")
        except Exception as e:
            self.stdout.write(e)

    COURSE_CATEGORIES = [
    "Programming", "Data Science", "Marketing", "Design",
    "Business", "Personal Development", "Photography", "Health & Fitness"
    ]

    def _add_categories(self):
        try:
            for course_name in self.COURSE_CATEGORIES:
                cat, created = Category.objects.get_or_create(
                    name=course_name
                )
                if created:
                    self.stdout.write(f'Category created: {cat.name}')

        except Exception as e:
            raise Exception(f"Error while creating category - {e}")
    
    def _add_course(self):
        try:
            user = User.objects.order_by('?').first()
            cat = Category.objects.order_by('?').first()
            course = Course.objects.create(
                author=user,
                name=fk.sentence(),
                category=cat,
                price=random.randint(100, 999)
            )
            course.save()
            self.stdout.write(f'Created course: {course.name}')
            modules_count = random.randint(4, 9)
            for i in range(modules_count):
                module = Module.objects.create(
                    name=fk.sentence(),
                    course=course
                )
                module.save()
                self.stdout.write(f"{i}. Module created for {course.name}")
                lesson_count = random.randint(3, 6)
                for x in range(lesson_count):
                    lesson = Lesson.objects.create(
                        name=fk.sentence(),
                        content=fk.paragraphs(),
                        module=module
                    )
                    lesson.save()
                    self.stdout.write(f'{x}.Lesson created for {module.name}')
        except Exception as e:
            raise Exception(f"Error while creating Course - {e}")