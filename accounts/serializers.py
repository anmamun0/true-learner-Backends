from rest_framework import serializers
from django.contrib.auth.models import User, Group

from .constraint import ROLE_CHOICES
from django.contrib.auth import authenticate

from .models import Student,Instructor


class RegistraionSerializer(serializers.ModelSerializer): 
    role = serializers.ChoiceField(choices=ROLE_CHOICES,required=True)
    phone = serializers.CharField(required=True)
    address = serializers.CharField(required=True)
    class Meta:
        model = User 
        fields = ['role','username','first_name','last_name','email','phone','address','password']

    def validate_username(self,value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError({'error_username':'username is already exist.',})
        return value
    def validate_email(self,value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError({'error_email':'email is already exist Account, Please login!'})
        return value 
    

class UserLoginSerializers(serializers.Serializer):
    email = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True,required=True)
    role = serializers.CharField(write_only=True,required=True)
    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        role = attrs.get('role')
        print(email,password,' ', role)
        try:
            user =  User.objects.get(email=email) 
        except Exception as e:
            raise serializers.ValidationError("The emal not exist any user")
        
        user = authenticate(username=user.username,password=password)
        if not user:
            raise serializers.ValidationError('Inalid User')
        if not user.is_active:
            raise serializers.ValidationError('User account is inactive!')
        
        if  not user.groups.filter(name=role).exists():
            raise serializers.ValidationError(f"You are not a {role}")
        if role == 'Student':
            attrs['profile'] = Student.objects.get(user=user)  
        elif role == 'Instructor':
            attrs['profile'] = Instructor.objects.get(user=user)  
        
        attrs['user'] = user
        return attrs
    
from .models import Instructor,Student
from courses.models import Course

class InstructorCourses(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields = "__all__"


class InstructorSerialisersProfile(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = ['title','image','bio','phone','address','total_students','expertise','years_of_experience','qualifications','website','facebook','twitter','linkedin']

class InstructorSerialisers(serializers.ModelSerializer):
    courses = InstructorCourses(read_only=True,many=True)

    instructor_profile = InstructorSerialisersProfile(read_only=True)  # Ensure the nested profile is included
    class Meta:
        model = User
        fields = ['id','username','first_name','last_name','email','groups','last_login','instructor_profile','courses']

from courses.models import Course
from payments.models import studentHistory

class studentHistroySerializers(serializers.ModelSerializer):
    class Meta:
        model = studentHistory
        fields = ['id','payment','course','enroll_type','created_on']

class CourseDetails(serializers.ModelSerializer): 
    class Meta:
        model = Course
        fields = "__all__" 

class StudentSerialisersProfile(serializers.ModelSerializer):
    courses = CourseDetails(many=True,read_only=True)
    class Meta:
        model = Student 
        fields = "__all__"

class StudentSerialisers(serializers.ModelSerializer):
    student_profile = StudentSerialisersProfile(read_only=True)  
    student_history = studentHistroySerializers(read_only=True,many=True)
    class Meta:
        model = User
        fields = ['id','username','first_name','last_name','email','groups','last_login','student_profile','student_history']