from rest_framework import serializers
from tasks_app.models import Task, Employee

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
