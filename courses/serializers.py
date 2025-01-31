from rest_framework import serializers
from .models import Course, Video ,Category


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

