from django import forms

from .models import Group, User, Student
from .models import Attendance, ExamResult

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['student', 'date', 'status']

class ExamResultForm(forms.ModelForm):
    class Meta:
        model = ExamResult
        fields = ['student', 'subject', 'score', 'date']


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'students']
        widgets = {
            'students': forms.CheckboxSelectMultiple(),  # SelectMultiple()
        }


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = []