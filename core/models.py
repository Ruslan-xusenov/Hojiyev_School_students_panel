from django.db import models
from accounts.models import User

class Attendance(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'student'})
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='attendances', limit_choices_to={'role': 'teacher'})
    date = models.DateField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student.username} - {self.date} - {'Keldi' if self.status else 'Kelmadi'}"

class ExamResult(models.Model):
    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'student'},
        related_name='exam_results'
    )
    teacher = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'teacher'},
        related_name='given_results'
    )
    subject = models.CharField(max_length=100)
    score = models.FloatField()
    date = models.DateField()

    def __str__(self):
        return f"{self.student.username} - {self.subject} - {self.score}"
    

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.get_full_name()

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.get_full_name()


class Group(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student, blank=True)

    def __str__(self):
        return self.name