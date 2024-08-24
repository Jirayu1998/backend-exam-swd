# views.py
from rest_framework import generics, filters
import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Teacher
from .serializers import TeacherListSerializer


class TeacherFilter(django_filters.FilterSet):
    classroom = django_filters.NumberFilter(field_name="classrooms", distinct=True)

    class Meta:
        model = Teacher
        fields = ["school", "classroom", "first_name", "last_name", "gender"]


class TeacherList(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherListSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = TeacherFilter
    search_fields = ["first_name", "last_name"]


class TeacherDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherListSerializer
