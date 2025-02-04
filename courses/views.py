from django.shortcuts import render
from rest_framework import viewsets ,status , response
from .serializers import CourseSerializers, VideoSerializes ,CategorySerializer ,EnrollmentStudents
# Create your views here.
from .models import Course,Video, Category

from .filters import CourseFilter
from django_filters import rest_framework

from rest_framework.decorators import action
from django.contrib.auth.models import User

from django.core.exceptions import ObjectDoesNotExist
from accounts.constraint import TOKEN_USER

class CourseView(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializers  
    filter_backends = (rest_framework.DjangoFilterBackend,)
    filterset_class = CourseFilter

    @action(detail=False, methods=['post'], url_path='create')
    def course_create(self, request):
        
        print('ye agaya')
        print(request.user.username)

        try:
            token_key = request.data.get('token')
            instructor = TOKEN_USER(token_key) 
            if not instructor.groups.filter(name='Instructor').exists(): 
                return response.Response({'error':"You'r not an Instructor"},status=status.HTTP_404_NOT_FOUND)

            print(instructor.username)
            # Extract data from the request
            title = request.data.get('title')
            thumble = request.data.get('thumble',None)
            category_ids = request.data.get('category', []) 
            description = request.data.get('description')  # Make sure the key matches
            price = request.data.get('price')
            total_lecture = request.data.get('total_lecture','')
            total_session = request.data.get('total_session','')
            total_length = request.data.get('total_length','')
            videos = request.data.get('videos',[])
            
            course = Course.objects.create(
                instructor= instructor,
                title=title,
                thumble=thumble, 
                description=description,
                price=price,
                total_lecture=total_lecture,
                total_session=total_session,
                total_length=total_length,
            )
            if category_ids:
                    course.category.set(Category.objects.filter(id__in=category_ids))
            course.save()


            if videos: 
                for video in videos:
                    v_title , v_url, v_duration = video.get('title'), video.get('url'), video.get('duration') 
                    if all([v_title, v_url, v_duration is not None]):
                        Video.objects.create(
                            course=course,
                            title=v_title,
                            url=v_url,
                            duration=v_duration,
                        )


            serializer = CourseSerializers(course)
            return response.Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return response.Response({'error':str(e)},status=status.HTTP_501_NOT_IMPLEMENTED)
        
        
    @action(detail=True,methods=['put'],url_path='update')
    def update_create(self,request,pk=None):
        try:
            course = Course.objects.get(pk=pk) 
            course.title = request.data.get('title',course.title)
            course.thumble = request.data.get('title',course.thumble)

            course.description = request.data.get('description',course.description)  # Make sure the key matches
            course.total_lecture = request.data.get('total_lecture',course.prtotal_lecturece)
            course.total_session = request.data.get('total_session',course.total_session)
            course.total_length = request.data.get('total_length',course.total_length) 
            course.save()
            
            serializer = CourseSerializers(course)
            return response.Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return response.Response({'error':str(e)},status=status.HTTP_501_NOT_IMPLEMENTED)
        
from .models import Course,Video
class VideoView(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializes

    @action(detail=True,methods=['post'],url_path='create')
    def video_create(self,request,pk=None):
        try:
            course = Course.objects.get(pk=pk)
            title = request.data.get('title')
            url = request.data.get('url') 
            video = Video.objects.create(
                course=course,
                title=title,
                url=url,
            )
            serializer = VideoSerializes(video)
            return response.Response(serializer.data,status=status.HTTP_201_CREATED)
        
        except Exception as e:
            return response.Response({'error':"invalid information!"},status=status.HTTP_400_BAD_REQUEST)
    @action(detail=True,methods=['put'],url_path='update')
    def video_update(self,request,pk=None):
        try:
            video = Video.objects.get(pk=pk)
            video.title = request.data.get('title',video.title)
            video.url = request.data.get('url',video.url)
            video.save()
            info = VideoSerializes(video)
            return response.Response(info.data,status=status.HTTP_200_OK)
        except Exception as e:
            return response.Response({'error':str(e)},status=status.HTTP_400_BAD_REQUEST)
        
    @action(detail=True,methods=['post'],url_path='delete')
    def video_delete(self,request,pk=None):
        try:
            video = Video.objects.get(pk=pk)
            video.delete()
            return response.Response({'message':"Successfully video deleted!"},status=status.HTTP_200_OK)
        except Exception as e:
            return response.Response({'error':str(e)},status=status.HTTP_400_BAD_REQUEST)
        


class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



class EnrollmentStudentsView(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = EnrollmentStudents