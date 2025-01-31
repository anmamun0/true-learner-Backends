from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseView ,VideoView,CategoryView

router = DefaultRouter()
router.register('courses',CourseView,basename='all_courses')
router.register('videos',VideoView,basename='all_videos')
router.register('category',CategoryView,basename='category')

urlpatterns = [
    path('',include(router.urls))
]