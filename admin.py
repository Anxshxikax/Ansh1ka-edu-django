from django.contrib import admin
from .models import Teacher, Student, Lesson

admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Lesson)

from .models import StudentProgress

admin.site.register(StudentProgress)
