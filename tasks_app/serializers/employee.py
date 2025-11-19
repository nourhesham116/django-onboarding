from rest_framework import serializers
from tasks_app.models import Employee

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
        fields = ['id', 'name', 'email', 'position', 'tasks']
