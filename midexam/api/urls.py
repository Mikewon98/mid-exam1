from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('student-list/', views.studentList, name="studentlist"),
    path('student-create/', views.studentCreate, name="studentcist")
]
