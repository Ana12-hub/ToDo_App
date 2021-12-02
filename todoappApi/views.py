from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view #To import the api data view
from rest_framework.response import Response   #To return responses to the browser
from .serializers import TaskSerializer   #To import the model data from the task list

from .models import Task
# Create your views here.
#The function todoappApiOverview will allow React js to get responses from the API
@api_view(['GET'])
def todoappApiOverview(request): #This function will display the app data in the django rest framework by using the urls.
	todoappApi_urls = {
		'List':'/task-list/',
		'Detail View':'/task-detail/<str:pk>/',
		'Create':'/task-create/',
		'Update':'/task-update/<str:pk>/',
		'Delete':'/task-delete/<str:pk>/',
		}

	return Response(todoappApi_urls)

#React js will get the data responses using the taskListfollowing functions
@api_view(['GET'])
def taskList(request):
	tasks = Task.objects.all().order_by('-id')
	serializer = TaskSerializer(tasks, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def taskDetail(request, pk):
	tasks = Task.objects.get(id=pk)
	serializer = TaskSerializer(tasks, many=False)
	return Response(serializer.data)

#The following are the functions created in the app to add and modify data in the class Task in models.
@api_view(['POST'])
def taskCreate(request):
	serializer = TaskSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def taskUpdate(request, pk):
	task = Task.objects.get(id=pk)
	serializer = TaskSerializer(instance=task, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def taskDelete(request, pk):
	task = Task.objects.get(id=pk)
	task.delete()

	return Response('Item succsesfully delete!')