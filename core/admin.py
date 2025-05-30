from django.contrib import admin
from .models import Attendance, ExamResult, Group, Student

admin.site.register(Group)
admin.site.register(Student)
admin.site.register(Attendance)
admin.site.register(ExamResult)