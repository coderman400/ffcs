# forms.py
from django import forms
from .models import Course,Slot

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['code', 'title']

class SlotsForm(forms.ModelForm):
    class Meta:
        model = Slot
        fields = ['course','prof','theory_slots','lab_slots']
