from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    region = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} - {self.region}"


class Student(models.Model):
    GRADE_CHOICES = [(str(i), f"Class {i}") for i in range(1, 6)]

    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    region = models.CharField(max_length=100)
    grade = models.CharField(max_length=2, choices=GRADE_CHOICES)
    assigned_teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.name} (Grade {self.grade})"


class Lesson(models.Model):
    SUBJECT_CHOICES = [
        ('Math', 'Mathematics'),
        ('EVS', 'Environmental Science'),
        ('Hindi', 'Hindi'),
        ('English', 'English'),
    ]

    title = models.CharField(max_length=200)
    subject = models.CharField(max_length=20, choices=SUBJECT_CHOICES)
    description = models.TextField()
    grade = models.CharField(max_length=2, choices=Student.GRADE_CHOICES)
    content_file = models.FileField(upload_to='lessons/')
    uploaded_by = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} - Grade {self.grade}"

class StudentProgress(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)
    completed_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('student', 'lesson')

    def __str__(self):
        return f"{self.student.name} - {self.lesson.title} - {'Done' if self.is_completed else 'Pending'}"
