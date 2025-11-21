from rest_framework import serializers
from tasks_app.models import Employee, Task


class EmployeeSerializer(serializers.ModelSerializer):
    """
    Serializer for Employee model.
    Includes related tasks (read-only) using related_name='tasks'.
    """
    tasks = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=True
    )

    class Meta:
        model = Employee
        fields = ['id', 'first_name', 'last_name', 'email', 'position', 'tasks']


class TaskSerializer(serializers.ModelSerializer):
    """
    Serializer for Task model.
    References employee by ID for assignment.
    """
    employee = serializers.PrimaryKeyRelatedField(
        queryset=Employee.objects.all()
    )

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'completed', 'employee', 'created_at', 'updated_at']
