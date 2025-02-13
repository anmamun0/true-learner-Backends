from django.urls import path , include
from .views import payment, success_view, fail_view, cancel_view , studentHistoryView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('',studentHistoryView)


urlpatterns = [
    path('pay/<int:user_id>/<int:course_id>/', payment, name='payment'),
    path('success/<int:user_id>/<int:course_id>', success_view, name='payment_success'), 
    path('fail/', fail_view, name='payment_fail'),
    path('cancel/', cancel_view, name='payment_cancel'),
    path('history/',include(router.urls))
]
