from django.db import models
from accounts.models import Student
from courses.models import Course 

# Create your models here.
class Progres(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE,related_name='student_progress')
    courses = models.ForeignKey(Course,on_delete=models.CASCADE,related_name='progress')
    video_list = models.JSONField(default=list, blank=True)
    enroll_date = models.DateField(auto_now_add=True)

    def update_progres(self,video_id):
        if video_id not in self.video_list:
            self.video_list.append(video_id)

    def __str__(self):
        return f"{self.courses.title}-({len(self.video_list)} watched)"