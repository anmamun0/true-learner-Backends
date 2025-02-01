from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseView ,VideoView,CategoryView,EnrollmentStudentsView

router = DefaultRouter()
router.register('courses',CourseView,basename='all_courses')
router.register('videos',VideoView,basename='all_videos')
router.register('category',CategoryView,basename='category')
router.register('paid_student',EnrollmentStudentsView,basename='paid_student')

urlpatterns = [
    path('',include(router.urls))
]