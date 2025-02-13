from rest_framework import serializers
from .models import studentHistory

class studentHistorySerializers(serializers.ModelSerializer):
    class Meta:
        model = studentHistory
        fields = "__all__"