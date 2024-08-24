from rest_framework import generics, filters
import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Student
from .serializers import StudentSerializer

class StudentFilter(django_filters.FilterSet):
    classroom = django_filters.NumberFilter(field_name="classroom", distinct=True)

    class Meta:
        model = Student
        fields = ["classroom__school", "classroom", "first_name", "last_name", 'gender']
        

class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = StudentFilter
    search_fields = ["first_name", "last_name"]
    
    
class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
