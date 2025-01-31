from django.urls import path
from .views import payment, success_view, fail_view, cancel_view

urlpatterns = [
    path('pay/<int:user_id>/<int:course_id>/', payment, name='payment'),
    path('success/<int:user_id>/<int:course_id>', success_view, name='payment_success'), 
    path('fail/', fail_view, name='payment_fail'),
    path('cancel/', cancel_view, name='payment_cancel'),
]
