from rest_framework import viewsets
from tasks_app.models import Employee
from tasks_app.serializers import EmployeeSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Employee model.
    Handles list, create, retrieve, update, and delete.
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'id'  # since Employee has manual PK
