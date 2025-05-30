from django.utils.dateparse import parse_date
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import GroupForm, StudentForm, UserForm,AttendanceForm, ExamResultForm
from .models import Student, Teacher, Group, Attendance, ExamResult, User

@login_required
def mark_attendance(request):
    if request.user.role != 'teacher':
        return redirect('dashboard')
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            attendance = form.save(commit=False)
            attendance.teacher = request.user
            attendance.save()
            return redirect('dashboard')
    else:
        form = AttendanceForm()
    return render(request, 'core/mark_attendance.html', {'form': form})


@login_required
def add_exam_result(request):
    if request.user.role != 'teacher':
        return redirect('dashboard')
    if request.method == 'POST':
        form = ExamResultForm(request.POST)
        if form.is_valid():
            result = form.save(commit=False)
            result.teacher = request.user
            result.save()
            return redirect('dashboard')
    else:
        form = ExamResultForm()
    return render(request, 'core/add_exam_result.html', {'form': form})


@login_required
def dashboard(request):
    if request.user.role == 'teacher':
        return render(request, 'core/teacher_dashboard.html')
    else:
        return render(request, 'core/student_dashboard.html')
    

@login_required
def student_attendance_view(request):
    date_filter = request.GET.get('date')
    attendance_list = Attendance.objects.filter(student=request.user)
    if date_filter:
        attendance_list = attendance_list.filter(date=parse_date(date_filter))
    return render(request, 'core/student_attendance.html', {'attendances': attendance_list})


@login_required
def student_exam_results_view(request):
    subject_filter = request.GET.get('subject')
    exam_results = ExamResult.objects.filter(student=request.user)
    if subject_filter:
        exam_results = exam_results.filter(subject__icontains=subject_filter)
    return render(request, 'core/student_results.html', {'results': exam_results})



@login_required
def create_group(request):
    teacher = Teacher.objects.get(user=request.user)
    
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            group = form.save(commit=False)
            group.teacher = teacher
            group.save()
            form.save_m2m()
            return redirect('dashboard')
    else:
        form = GroupForm()
    
    return render(request, 'accounts/create_group.html', {'form': form})



def add_student(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        student_form = StudentForm(request.POST)
        if user_form.is_valid() and student_form.is_valid():
            user = user_form.save()
            student = student_form.save(commit=False)
            student.user = user
            student.save()
            return redirect('student_list')
    else:
        user_form = UserForm()
        student_form = StudentForm()
    
    return render(request, 'teacher/add_student.html', {
        'user_form': user_form,
        'student_form': student_form
    })

def add_group(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            group = form.save(commit=False)
            group.teacher = request.user
            group.save()
            return redirect('group_list')
    else:
        form = GroupForm()
    return render(request, 'teacher/add_group.html', {'form': form})


@login_required
def my_groups(request):
    student = Student.objects.get(user=request.user)
    groups = Group.objects.filter(students=student)
    return render(request, 'core/my_groups.html', {'groups': groups})


@login_required
def add_students_to_group(request, group_id):
    teacher = Teacher.objects.get(user=request.user)
    group = Group.objects.get(id=group_id, teacher=teacher)
    if request.method == 'POST':
        form = GroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = GroupForm(instance=group)
    return render(request, 'core/add_students_to_group.html', {'form': form, 'group': group})
