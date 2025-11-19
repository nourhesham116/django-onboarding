from rest_framework import viewsets
from tasks_app.models import Task
from tasks_app.serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Task model.
    Handles list, create, retrieve, update, and delete.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
