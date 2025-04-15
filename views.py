from django.shortcuts import render, get_object_or_404
from .models import Student, Lesson, Teacher

def home(request):
    return render(request, 'education/home.html')

def student_list(request):
    students = Student.objects.all()
    return render(request, 'education/student_list.html', {'students': students})

def lesson_list(request):
    lessons = Lesson.objects.all()
    return render(request, 'education/lesson_list.html', {'lessons': lessons})

def lesson_detail(request, lesson_id):
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    return render(request, 'education/lesson_detail.html', {'lesson': lesson})

def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'education/teacher_list.html', {'teachers': teachers})
