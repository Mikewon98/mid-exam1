from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import studentSerializer
# Create your views here.

from .models import Student


@api_view(['GET'])
def apiOverview(request):

    api_urls = {
        'List': '/list',
        'Create': '/create',
    }

    return Response(api_urls)


@api_view(['GET'])
def studentList(request):
    student = Student.objects.all()
    serializer = studentSerializer(student, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def studentCreate(request):
    serializer = studentSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)
