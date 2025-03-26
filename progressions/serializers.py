from .models import Progres
from rest_framework import serializers

class ProgressSerializers(serializers.ModelSerializer):
    total_video = serializers.SerializerMethodField()

    class Meta:
        model = Progres
        fields = ['id','student','course','video_list','total_video']

    def get_total_video(self,obj):
        return obj.course.videos.count()