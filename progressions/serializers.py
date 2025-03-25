from .models import Progres
from rest_framework import serializers

class ProgressSerializers(serializers.ModelSerializer):
    class Meta:
        model = Progres
        fields = "__all__"
        