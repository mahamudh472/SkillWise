SkillWise DRF Project – Developer Testing Checklist
===================================================

✅ Authentication & Permissions
-------------------------------
[ ] User registration with email verification
[ ] JWT login/logout system
[ ] Role-based permission logic (Student, Instructor, Admin)
[ ] Password reset (via email token or link)
[ ] Block unauthorized access to restricted endpoints

✅ User & Profile Features
--------------------------
[ ] Profile view & update (name, avatar, bio)
[ ] View own enrolled courses
[ ] Track learning progress (completed lessons/modules)
[ ] View purchase history

✅ Course Management (Instructor)
---------------------------------
[ ] Create/update/delete course
[ ] Add modules and lessons under a course
[ ] Upload lesson content (text, video links, files optional)
[ ] Publish/unpublish course
[ ] Instructor dashboard with stats (sales, reviews, students)

✅ Course Consumption (Student)
-------------------------------
[ ] List available courses (with pagination, search, filtering)
[ ] View single course with module/lesson breakdown
[ ] Enroll in course (paid + free)
[ ] Progress tracking (mark lesson/module as completed)
[ ] Leave a review and rating
[ ] View own review/edit it

✅ Admin Dashboard
------------------
[ ] View all users (with roles and filters)
[ ] Block/unblock or delete users
[ ] View course analytics (sales, most popular, revenue)
[ ] Manage categories and tags
[ ] View and manage payment records

✅ Payment System
-----------------
[ ] Integrate with Stripe or SSLCOMMERZ sandbox
[ ] Start payment intent/transaction
[ ] Verify payment via webhook
[ ] Save invoice and payment record
[ ] Restrict course access until payment is confirmed

✅ API Features
---------------
[ ] All endpoints return proper HTTP codes (200, 400, 403, 401, 404, 500)
[ ] Pagination, filtering, and search work on listings
[ ] Swagger/OpenAPI docs available at `/api/docs/`
[ ] Token expiry handling is tested
[ ] Rate limiting/throttling (optional)

✅ Performance & Security
--------------------------
[ ] select_related & prefetch_related used in serializers
[ ] Caching implemented on public course list
[ ] Indexes added on foreign key and frequently queried fields
[ ] Sensitive actions protected with proper permissions
[ ] CSRF and CORS properly handled
[ ] Static/media file protection for private content

✅ Code Quality & Maintenance
-----------------------------
[ ] Organized app structure (`users`, `courses`, `payments`, etc.)
[ ] Serializers are modular and well-named
[ ] Models have `__str__`, verbose_name, Meta options
[ ] Custom exceptions and clean error messages
[ ] Signals or post-save hooks used cleanly (e.g., after payment)
[ ] All major features tested via API or unit tests

✅ Deployment Readiness (Optional)
---------------------------------
[ ] `.env` used for sensitive settings
[ ] DRF settings separated in `settings.py`
[ ] Production-ready security settings checked (DEBUG=False)
[ ] Email sending (SMTP or console) tested
[ ] Logs print helpful info/errors

