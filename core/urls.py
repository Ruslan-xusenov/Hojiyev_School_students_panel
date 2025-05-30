from django.urls import path
from django.contrib.auth import views as auth_views
from .views import mark_attendance, add_exam_result, dashboard, student_attendance_view, student_exam_results_view, my_groups

urlpatterns = [
    path('attendance/', mark_attendance, name='mark_attendance'),
    path('exam-result/', add_exam_result, name='add_exam_result'),
    path('dashboard/', dashboard, name='dashboard'),
    path('my-attendance/', student_attendance_view, name='my_attendance'),
    path('my-results/', student_exam_results_view, name='my_results'),
    path('my-groups/', my_groups, name='my_groups'),
]