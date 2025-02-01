from rest_framework import serializers
from .models import Course, Video ,Category

from accounts.models import Student
from django.contrib.auth.models import User

class CategorySerializer(serializers.ModelSerializer):
    # Define course_count as a SerializerMethodField
    course_count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'course_count']

    def get_course_count(self, obj):
        # Return the count of courses related to the category
        return obj.course.count()

class VideoSerializes(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = "__all__"
 

class CourseSerializers(serializers.ModelSerializer):
    videos = VideoSerializes(read_only=True,many=True) 
    category = serializers.StringRelatedField(many=True)  
    students = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ['code','thumble','category','students','title','description','total_lecture','total_session','total_length','total_student','price','instructor','created_on','videos']

    def get_students(self,obj):
        return obj.students.count()



class EnrollUser(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']  # Typo: 'fileds' should be 'fields'


class EnrollStudent(serializers.ModelSerializer):
    user = EnrollUser(read_only=True)
    class Meta:
        model = Student
        fields = ['user','image','bio','phone','address','facebook','twitter','linkedin']

class EnrollmentStudents(serializers.ModelSerializer):
    students = EnrollStudent(read_only=True,many=True)
    class Meta:
        model = Course
        fields = ['code','students']