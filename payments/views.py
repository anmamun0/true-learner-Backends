from django.http import HttpResponse ,JsonResponse
from django.shortcuts import redirect, render

from rest_framework.response import Response

from sslcommerz_lib import SSLCOMMERZ
import uuid  # To generate unique transaction ID
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
  
from datetime import datetime
from rest_framework.decorators import api_view
from courses.models import Course
from .models import studentHistory

from progressions.models import Progres

@csrf_exempt
def payment(request,user_id,course_id):
    if request.method != "POST":
        return JsonResponse({"error": "Invalid request method"}, status=405)
    course = Course.objects.get(code=course_id)
    if(course.price<=0):
        return success_view(request,user_id,course_id) 

     
    settings = {
        'store_id': 'ancod6799f7f3afcfa',
        'store_pass': 'ancod6799f7f3afcfa@ssl',
        'issandbox': True  # Set to False for production
    } 

    try:
        user = User.objects.get(pk=user_id)  # Ensure user exists
    except User.DoesNotExist:
        return JsonResponse({"error": "User not found"}, status=404)

    sslcz = SSLCOMMERZ(settings)

    # Generate unique transaction ID
    transaction_id = str(uuid.uuid4())

    post_body = {
        'total_amount': 100.26,
        'currency': "BDT",
        'tran_id': transaction_id,  # Unique transaction ID
        'success_url': f"https://truelearner-backends.onrender.com/payment/success/{user_id}/{course_id}",
        'fail_url': "https://truelearner-backends.onrender.com/payment/fail/",
        'cancel_url': "https://truelearner-backends.onrender.com/payment/cancel/",
        'emi_option': 0,
        'cus_name': user.username,
        'cus_email': user.email,
        'cus_phone': "01700000000",
        'cus_add1': "customer address",
        'cus_city': "Dhaka",
        'cus_country': "Bangladesh",
        'shipping_method': "NO",
        'multi_card_name': "",
        'num_of_item': 1,
        'product_name': "Test",
        'product_category': "Test Category",
        'product_profile': "general"
    }

    response = sslcz.createSession(post_body)  # API response
 
    if 'GatewayPageURL' in response:
        return JsonResponse({"url": response['GatewayPageURL']})  # Send URL as JSON
    else:
        return JsonResponse({"error": "Payment gateway initialization failed"}, status=400)


@csrf_exempt
def success_view(request, user_id,course_id):
    print('success view', user_id,'asd',course_id)
    try:
        user = User.objects.get(id=int(user_id))  # Ensure `user_id` is an integer
        course = Course.objects.get(code=course_id)
        course.total_student += 1
        course.save()

        user.student_profile.courses.add(course)
        Progres.objects.create(student=user.student_profile,course=course)
        print('progres created')


        instructor = course.instructor.instructor_profile
        instructor.total_students += 1
        instructor.save()

        studentHistory.objects.create(
            user=user,
            course=course,
            payment=course.price,
            enroll_type = "Free" if course.price==0 else "Paid"
        )
        
    except User.DoesNotExist:
        return HttpResponse("User not found.", status=404)
    context = {
        'course_title':course.title,
        'instructor_name':course.instructor.username,
        'course_price':course.price,
        'discount':0,
        'total_amount':course.price,
        'transaction_id':'048573', 
        'payment_date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 
    }
    return render(request,'payment_success.html',context)
    # return HttpResponse(f"Payment successful for {user.username}", status=200)




# @api_view(['GET'])
# def success_view(request, user_id):
#     print('success view', user_id)
    
#     try:
#         user = User.objects.get(id=int(user_id))  # Ensure `user_id` is an integer
#     except User.DoesNotExist:
#         return Response({"error": "User not found."}, status=404)

#     return Response({
#         "message": "Payment successful",
#         "user": {
#             "id": user.id,
#             "username": user.username,
#             "email": user.email
#         }
#     }, status=200)

@csrf_exempt
def fail_view(request):  
    context = { 
        'payment_date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 
    }
    return render(request,'payment_fail.html',context) 

 

# @csrf_exempt
# def payment(request, user_id):
#     print('abcd',user_id)
#     settings = {
#         'store_id': 'ancod6799f7f3afcfa',
#         'store_pass': 'ancod6799f7f3afcfa@ssl',
#         'issandbox': True  # Set to False for production
#     } 
#     try:
#         user = User.objects.get(pk=user_id)  # Fix: Use `id=int(user_id)` 
#     except User.DoesNotExist:
#         return HttpResponse("User -- not found.", status=404)

#     sslcz = SSLCOMMERZ(settings)

#     # Generate unique transaction ID
#     transaction_id = str(uuid.uuid4())

#     post_body = {
#         'total_amount': 100.26,
#         'currency': "BDT",
#         'tran_id': transaction_id,  # Use unique transaction ID
#         'success_url': f"http://127.0.0.1:8000/payment/success/{user_id}",
#         'fail_url': "http://127.0.0.1:8000/payment/fail/",
#         'cancel_url': "http://127.0.0.1:8000/payment/cancel/",
#         'emi_option': 0,
#         'cus_name': user.username,
#         'cus_email': user.email,
#         'cus_phone': "01700000000",
#         'cus_add1': "customer address",
#         'cus_city': "Dhaka",
#         'cus_country': "Bangladesh",
#         'shipping_method': "NO",
#         'multi_card_name': "",
#         'num_of_item': 1,
#         'product_name': "Test",
#         'product_category': "Test Category",
#         'product_profile': "general"
#     }

#     response = sslcz.createSession(post_body)  # API response
#     print('asdf',user.username)

#     if 'GatewayPageURL' in response:
#         return redirect(response['GatewayPageURL'])  # Redirect user to payment page
#     else:
#         return HttpResponse("Payment gateway initialization failed.", status=400)

from rest_framework.response import Response
from django.contrib.auth.models import User



# @csrf_exempt
# def success_view(request, user_id):
#     print('success view', user_id)
#     try:
#         user = User.objects.get(id=int(user_id))  # Ensure `user_id` is an integer
#     except User.DoesNotExist:
#         return HttpResponse("User not found.", status=404)

#     return HttpResponse(f"Payment successful for {user.username}", status=200)




# def fail_view(request):
#     return HttpResponse("Payment failed.", status=400)

def cancel_view(request):
    return HttpResponse("Payment canceled.")









from .serializers import studentHistorySerializers
from .models import studentHistory
from rest_framework.viewsets import ModelViewSet
from django_filters import rest_framework
from .filters import studentHistoryFilter


class studentHistoryView(ModelViewSet):
    queryset = studentHistory.objects.all()
    serializer_class = studentHistorySerializers

    filter_backends = (rest_framework.DjangoFilterBackend,)
    filterset_class =studentHistoryFilter