from django.db import models


class School(models.Model):
    name = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=20)
    address = models.TextField()

    class Meta:
        db_table = "school"

    def __str__(self):
        return self.name


class Classroom(models.Model):
    school = models.ForeignKey(
        School, on_delete=models.CASCADE, related_name="classrooms"
    )
    grade = models.IntegerField()
    room = models.CharField(max_length=10)
    teachers = models.ManyToManyField("Teacher", related_name="classrooms")

    class Meta:
        db_table = "classroom"
        unique_together = ("school", "grade", "room")

    def __str__(self):
        return f"{self.school.abbreviation} - ชั้น {self.grade}/{self.room}"


class Teacher(models.Model):
    GENDER_CHOICES = [
        ("M", "ชาย"),
        ("F", "หญิง"),
        ("O", "อื่นๆ"),
    ]
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    school = models.ForeignKey(
        School, on_delete=models.CASCADE, related_name="teachers"
    )

    class Meta:
        db_table = "teacher"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Student(models.Model):
    GENDER_CHOICES = [
        ("M", "ชาย"),
        ("F", "หญิง"),
        ("O", "อื่นๆ"),
    ]
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    classroom = models.ForeignKey(
        Classroom, on_delete=models.CASCADE, related_name="students"
    )

    class Meta:
        db_table = "student"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
