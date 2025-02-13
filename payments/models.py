from django.db import models
from django.contrib.auth.models import User , Group
from courses.models import Course
# Create your models here.
class studentHistory(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='student_history')
    course = models.ForeignKey(Course,on_delete=models.SET_NULL,null=True)
    payment = models.CharField(max_length=12)
    enroll_type = models.CharField(max_length=20) 
    created_on = models.DateTimeField(auto_now_add=True)    

    class Meta:
        ordering = ["-created_on"]

class instructorHistory(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='instructor_history')
    course = models.ForeignKey(Course,on_delete=models.SET_NULL,null=True)
    created_on = models.DateTimeField(auto_now_add=True)    

