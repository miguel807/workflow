from django.db import models
from river.models.fields.state import StateField
from river.models import State

# Create your models here.


class StudentModel(models.Model):
    """Model definition for EstudentModel."""
    name = models.CharField(max_length=50,unique=True)
    term = models.CharField(max_length=30)
    grade = models.IntegerField(default=1)
    student_state_field = StateField() 
    
    
    class Meta:
        """Meta definition for EstudentModel."""

        verbose_name = 'EstudentModel'
        verbose_name_plural = 'EstudentModels'

    def __str__(self):
        """Unicode representation of EstudentModel."""
        return self.name


