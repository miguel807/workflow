from rest_framework import viewsets
from rest_framework.response import Response
from .models import StudentModel
from .serializer import StudenteCreateSerializer
from rest_framework.decorators import action
from django.contrib.auth.models import User
from river.models import State
import random



class StudentViewSet(viewsets.ModelViewSet):
    basename = 'student'
    serializer_class = StudenteCreateSerializer

    @action(detail=False, methods=['post'])
    def iniciar_workflow(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            name = request.data.get('name',"")
            student  = StudentModel.objects.get(name = name)  
            super_user = User.objects.get(id=1)
            student.river.student_state_field.approve(as_user=super_user)       
            return Response({'status': 'Workflow init'})
        return Response({"error":"Error"})

        
    

