from django import forms
from .models import Task

#here we declare model creation class 
class TaskCreate(forms.ModelForm):

	class Meta:
		model = Task
		fields = '__all__'
		