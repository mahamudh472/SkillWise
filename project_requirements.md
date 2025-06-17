SkillWise – Course Selling Platform API
========================================

Project Summary
---------------
SkillWise is an online learning platform backend built using Django REST Framework.  
It will serve as the API for a mobile app that allows users to explore and purchase courses,  
track their learning progress, and interact with instructors. Instructors can manage courses,  
upload content, and view earnings. Admins have full control over the platform.

User Roles
----------
- Guest: Can view courses and register/login.
- User (Student): Can enroll in courses, track progress, leave reviews.
- Instructor: Can create/edit courses and view stats.
- Admin: Full access including analytics, user management.

Key Features
------------
- JWT Authentication (Login, Signup, Password Reset)
- Role-Based Access and Permissions
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

Example Use Cases
-----------------
1. A user signs up, verifies email, browses courses, and purchases a course via Stripe.
2. An instructor logs in, creates a course, uploads lessons, and publishes it.
3. A user completes lessons, tracks progress, and leaves a review.
4. Admin views analytics: top courses, most active users, total earnings.

Endpoints Overview (Examples)
-----------------------------
- /api/v1/auth/register/            -> Signup
- /api/v1/auth/login/               -> Login
- /api/v1/courses/                  -> List/Create Courses
- /api/v1/courses/{id}/             -> Retrieve Course Details
- /api/v1/enrollments/              -> Enroll in a Course
- /api/v1/progress/                 -> Track User Progress
- /api/v1/payments/create/          -> Initiate Payment
- /api/v1/instructors/dashboard/    -> Instructor Stats
- /api/v1/reviews/                  -> Post a Course Review
- /api/v1/admin/analytics/          -> Admin Analytics

Payment System
--------------
- Integrate with Stripe or SSLCOMMERZ
- Webhook listener to verify payment
- Store invoices and purchase history
- Secure and idempotent payment logic

Performance Optimization
------------------------
- Use select_related, prefetch_related
- Add indexes to important fields (e.g., user_id, course_id)
- Cache course list endpoint for anonymous users
- Use DRF pagination and query optimization
