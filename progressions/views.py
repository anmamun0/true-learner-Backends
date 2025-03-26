from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from .models import Progres
from .serializers import ProgressSerializers
from django_filters import rest_framework
from .filters import ProgressFilter

from rest_framework.response import Response
from rest_framework import status

class ProgressViewSerializers(ModelViewSet):
    queryset = Progres.objects.all()
    serializer_class = ProgressSerializers

    filter_backends = (rest_framework.DjangoFilterBackend,)
    filterset_class = ProgressFilter
    
    @action(detail=True,methods=['post'],url_path='update')
    def update_progress(self,request,pk=None):
        progres = Progres.objects.get(pk=pk)
        video_id = request.data.get('video_id')
        progres.update_progres(video_id)
        progres.save()
        
        print('reseive->',video_id)
        return Response('Successfully received vide_id',status=status.HTTP_200_OK)


