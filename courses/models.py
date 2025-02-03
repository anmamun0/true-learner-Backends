from django.db import models
from django.contrib.auth.models import User , Group

class Category(models.Model):
    name = models.CharField(max_length=40)
    slug = models.SlugField()

    def __str__(self):
        return self.name
    def course_count(self):
        return self.course.count()
    

class Course(models.Model):
    code = models.AutoField(primary_key=True)
    instructor = models.ForeignKey(User,on_delete=models.CASCADE,related_name='courses')
    thumble = models.URLField(max_length=100,null=True,blank=True)
    category = models.ManyToManyField(Category,related_name='course')
    title  = models.CharField(max_length=50)
    description = models.TextField()
    price = models.IntegerField()
    created_on = models.DateField(auto_now_add=True) 
    total_lecture = models.IntegerField(null=True,blank=True)
    total_session = models.IntegerField(null=True,blank=True)
    total_length = models.IntegerField(null=True,blank=True)
    total_student = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
    
    def progress(self):
        total = self.videos.count()
        if total == 0:
            return 0
        completed = self.videos.filter(view=True).count()
        return int((completed  / total) * 100)
    
class Video(models.Model):
    order = models.AutoField(primary_key=True)  
    course = models.ForeignKey(Course,on_delete=models.CASCADE,related_name='videos')
    title = models.CharField(max_length=100)
    url = models.URLField(max_length=150)  
    duration = models.CharField(max_length=8,null=True,blank=True)
    
    class Meta:
        ordering = ['order']
    def __str__(self):
        return self.title
    