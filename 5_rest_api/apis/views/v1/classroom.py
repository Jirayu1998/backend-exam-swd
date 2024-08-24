from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .models import Classroom
from .serializers import ClassroomListSerializer, ClassroomDetailSerializer


class ClassroomList(generics.ListCreateAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["school"]


class ClassroomDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomDetailSerializer
