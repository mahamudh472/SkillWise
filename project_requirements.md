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

## 📌 Authentication & User Management

* `POST /api/v1/auth/register/` → User signup
* `POST /api/v1/auth/login/` → Obtain JWT token
* `POST /api/v1/auth/logout/` → Invalidate token
* `POST /api/v1/auth/refresh/` → Refresh JWT token
* `POST /api/v1/auth/password-reset/` → Request reset link
* `POST /api/v1/auth/password-reset/confirm/` → Confirm new password
* `GET  /api/v1/profile/` → Get own profile
* `PATCH /api/v1/profile/` → Update own profile
* `GET  /api/v1/users/{id}/` → (Admin) Get user details
* `PATCH /api/v1/users/{id}/` → (Admin) Update user
* `DELETE /api/v1/users/{id}/` → (Admin) Delete user

---

## 📌 Courses & Content

* `GET  /api/v1/courses/` → List all courses (filtering, search, pagination)
* `POST /api/v1/courses/` → (Instructor/Admin) Create course
* `GET  /api/v1/courses/{id}/` → Get course details
* `PATCH /api/v1/courses/{id}/` → (Instructor/Admin) Update course
* `DELETE /api/v1/courses/{id}/` → (Instructor/Admin) Delete course

**Modules inside a course**

* `POST /api/v1/courses/{course_id}/modules/` → Add module
* `GET  /api/v1/courses/{course_id}/modules/` → List modules
* `PATCH /api/v1/modules/{id}/` → Update module
* `DELETE /api/v1/modules/{id}/` → Delete module

**Lessons inside a module**

* `POST /api/v1/modules/{module_id}/lessons/` → Add lesson
* `GET  /api/v1/modules/{module_id}/lessons/` → List lessons
* `GET  /api/v1/lessons/{id}/` → Lesson detail (content, video, attachments)
* `PATCH /api/v1/lessons/{id}/` → Update lesson
* `DELETE /api/v1/lessons/{id}/` → Delete lesson

---

## 📌 Enrollment & Progress

* `POST /api/v1/courses/{id}/enroll/` → Enroll in a course (after payment)
* `GET  /api/v1/enrollments/` → My enrollments
* `GET  /api/v1/enrollments/{id}/` → Enrollment details (status, started\_at, progress)
* `PATCH /api/v1/enrollments/{id}/progress/` → Update progress (mark lesson as complete)
* `GET  /api/v1/progress/{course_id}/` → Track progress per course

---

## 📌 Payments

* `POST /api/v1/payments/create/` → Initiate payment (Stripe/SSLCOMMERZ)
* `POST /api/v1/payments/webhook/` → Webhook to verify payment
* `GET  /api/v1/payments/history/` → My payment history
* `GET  /api/v1/payments/invoices/{id}/` → Download/view invoice

---

## 📌 Reviews & Ratings

* `POST /api/v1/courses/{id}/reviews/` → Add review to course
* `GET  /api/v1/courses/{id}/reviews/` → List course reviews
* `PATCH /api/v1/reviews/{id}/` → Update review
* `DELETE /api/v1/reviews/{id}/` → Delete review

---

## 📌 Instructor Dashboard

* `GET  /api/v1/instructors/dashboard/` → Stats (earnings, enrolled students, active courses)
* `GET  /api/v1/instructors/courses/` → List courses by instructor
* `GET  /api/v1/instructors/courses/{id}/students/` → Enrolled students in a course
* `GET  /api/v1/instructors/earnings/` → Earnings history

---

## 📌 Admin Dashboard

* `GET  /api/v1/admin/analytics/` → Platform-wide stats
* `GET  /api/v1/admin/courses/` → Manage all courses
* `GET  /api/v1/admin/users/` → Manage all users
* `GET  /api/v1/admin/payments/` → Payment logs
* `GET  /api/v1/admin/reports/` → Reported content/users

---

## 📌 Notifications

* `GET  /api/v1/notifications/` → List my notifications
* `PATCH /api/v1/notifications/{id}/read/` → Mark as read

---

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
