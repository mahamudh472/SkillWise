from django.core.management.base import BaseCommand, CommandError
from accounts.models import User 
from core.models import Category, Course, Module, Lesson
import faker, random
fk = faker.Faker()

class Command(BaseCommand):
    help = "populate database tables with dummy data"

    def handle(self, *args, **options):
        
        try:
            self._add_course()
        except Exception as e:
            raise CommandError(f'An error occured {e}')
        
    
    # Helper functions
    def _add_user(self):
        try:
            user = User.objects.create_user(
                username=fk.user_name(),
                email=fk.email(),
                first_name=fk.first_name(),
                last_name=fk.last_name(),
                password="1234"
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