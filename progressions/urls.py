from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import ProgressViewSerializers

router = DefaultRouter()
router.register('',ProgressViewSerializers,basename='progressview')


urlpatterns = [
    path('all/',include(router.urls))
]