from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.v1.school import SchoolList, SchoolDetail
from .views.v1.classroom import ClassroomList, ClassroomDetail
from .views.v1.teacher import TeacherList, TeacherDetail
from .views.v1.student import StudentList, StudentDetail

router = DefaultRouter()

api_v1_urls = (router.urls, "v1")

urlpatterns = [
    path("v1/", include(api_v1_urls)),
    # api school
    path("v1/schools/", SchoolList.as_view(), name="school-list"),
    path("v1/schools/<int:pk>/", SchoolDetail.as_view(), name="school-detail"),
    # api classroom
    path("v1/classrooms/", ClassroomList.as_view(), name="classroom-list"),
    path("v1/classrooms/<int:pk>/", ClassroomDetail.as_view(), name="classroom-detail"),
    # api teacher
    path("v1/teachers/", TeacherList.as_view(), name="teacher-list"),
    path("v1/teachers/<int:pk>/", TeacherDetail.as_view(), name="teacher-detail"),
    # api student
    path("v1/students/", StudentList.as_view(), name="student-list"),
    path("v1/students/<int:pk>/", StudentDetail.as_view(), name="student-detail"),
]
