from rest_framework import serializers
from .models import StudentModel

class StudenteCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentModel
        fields = ['name']