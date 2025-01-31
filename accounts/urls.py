from django.urls import path , include
from rest_framework.routers import DefaultRouter
from .views import RegistrationView ,LoginView ,LogoutView ,activate,InstructorView ,StudentView

router = DefaultRouter()
router.register('instructors',InstructorView,basename='instructors')
router.register('students',StudentView,basename='students')

urlpatterns = [
    path('register/',RegistrationView.as_view(),name='register'),
    path('login/',LoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('activate/<uid64>/<token>',activate,name='activate'),
    path('',include(router.urls))
]