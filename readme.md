# SkillWise – Course Selling Platform API

SkillWise is an online learning platform backend built using Django REST Framework. It provides a robust API for a mobile or web app, enabling users to explore and purchase courses, track learning progress, and interact with instructors. Instructors can manage courses and content, while admins have full control over the platform.

## Features
- JWT Authentication (Login, Signup, Password Reset)
- Role-Based Access and Permissions (Student, Instructor, Admin)
- Course Management (Course > Module > Lesson)
- Payment Integration (Stripe or SSLCOMMERZ)
- Review and Rating System
- Profile and Progress Tracking
- Instructor and Admin Dashboards
- Search, Filtering, Pagination
- Caching and Database Optimization
- Email Notifications (via Celery)
- API Documentation (Swagger/OpenAPI)
- Unit Testing

## User Roles
- **Guest:** View courses, register/login
- **Student:** Enroll in courses, track progress, leave reviews
- **Instructor:** Create/edit courses, view stats
- **Admin:** Full access, analytics, user management

## Example Use Cases
1. A user signs up, verifies email, browses courses, and purchases a course via Stripe.
2. An instructor logs in, creates a course, uploads lessons, and publishes it.
3. A user completes lessons, tracks progress, and leaves a review.
4. Admin views analytics: top courses, most active users, total earnings.

## API Endpoints (Examples)
- `POST   /api/v1/auth/register/`            – Signup
- `POST   /api/v1/auth/login/`               – Login
- `GET    /api/v1/courses/`                  – List/Create Courses
- `GET    /api/v1/courses/{id}/`             – Retrieve Course Details
- `POST   /api/v1/enrollments/`              – Enroll in a Course
- `GET    /api/v1/progress/`                 – Track User Progress
- `POST   /api/v1/payments/create/`          – Initiate Payment
- `GET    /api/v1/instructors/dashboard/`    – Instructor Stats
- `POST   /api/v1/reviews/`                  – Post a Course Review
- `GET    /api/v1/admin/analytics/`          – Admin Analytics
- API docs: `/api/docs/swagger/` (Swagger UI), `/api/docs/redoc/` (ReDoc)

## Project Structure
- `accounts/` – User, profile, authentication, permissions
- `core/` – Courses, modules, lessons, enrollments, payments, reviews
- `SkillWise/` – Project settings and URLs

## Setup Instructions
1. **Clone the repository:**
   ```bash
   git clone https://github.com/mahamudh472/SkillWise.git
   cd SkillWise
   ```
2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv env
   source env/bin/activate
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```
5. **Create a superuser (admin):**
   ```bash
   python manage.py createsuperuser
   ```
6. **(Optional) Seed the database with demo data:**
   ```bash
   python manage.py seed_db
   ```
7. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

## Running Tests
```bash
python manage.py test
```

## API Documentation
- Swagger UI: [http://localhost:8000/api/docs/swagger/](http://localhost:8000/api/docs/swagger/)
- ReDoc: [http://localhost:8000/api/docs/redoc/](http://localhost:8000/api/docs/redoc/)

## Contribution Guidelines
- Fork the repo and create a feature branch.
- Write clear commit messages and add tests for new features.
- Ensure code passes linting and tests before submitting a PR.

## License
MIT License

---
For more details, see `project_requirements.md` and `checklist.md` for developer and deployment checklists.
