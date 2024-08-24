from rest_framework import serializers
from .models import School, Classroom, Teacher, Student


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ["id", "first_name", "last_name"]


class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ["id", "grade", "room"]


class StudentSerializerForClassroom(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ["id", "first_name", "last_name", "gender"]


class SchoolSerializer(serializers.ModelSerializer):
    classroom_count = serializers.SerializerMethodField()
    teacher_count = serializers.SerializerMethodField()
    student_count = serializers.SerializerMethodField()

    class Meta:
        model = School
        fields = [
            "id",
            "name",
            "abbreviation",
            "address",
            "classroom_count",
            "teacher_count",
            "student_count",
        ]

    def get_classroom_count(self, obj):
        return obj.classrooms.count()

    def get_teacher_count(self, obj):
        return obj.teachers.count()

    def get_student_count(self, obj):
        return sum(classroom.students.count() for classroom in obj.classrooms.all())


class SchoolListSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ["id", "name", "abbreviation", "address"]


class ClassroomListSerializer(serializers.ModelSerializer):
    school_name = serializers.CharField(source="school.name", read_only=True)

    class Meta:
        model = Classroom
        fields = ["id", "grade", "room", "school", "school_name"]


class ClassroomDetailSerializer(serializers.ModelSerializer):
    teachers = TeacherSerializer(many=True, read_only=True)
    students = StudentSerializerForClassroom(many=True, read_only=True)
    school_name = serializers.CharField(source="school.name", read_only=True)

    class Meta:
        model = Classroom
        fields = [
            "id",
            "grade",
            "room",
            "school",
            "school_name",
            "teachers",
            "students",
        ]


class TeacherListSerializer(serializers.ModelSerializer):
    school_name = serializers.CharField(source="school.name", read_only=True)
    classrooms = ClassroomSerializer(many=True, read_only=True)

    class Meta:
        model = Teacher
        fields = [
            "id",
            "first_name",
            "last_name",
            "gender",
            "school",
            "school_name",
            "classrooms",
        ]


class StudentSerializer(serializers.ModelSerializer):
    classroom = ClassroomListSerializer(read_only=True)

    class Meta:
        model = Student
        fields = ["id", "first_name", "last_name", "gender", "classroom"]
