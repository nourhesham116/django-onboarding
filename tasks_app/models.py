from django.db import models


class Employee(models.Model):
    """
    Employee model representing a staff member.
    Primary key is manually assigned via 'id'.
    """
    id = models.CharField(
        max_length=10,
        primary_key=True,
        help_text="Manual employee ID (you assign it)"
    )
    first_name = models.CharField(max_length=50, help_text="First name of the employee")
    last_name = models.CharField(max_length=50, help_text="Last name of the employee")
    email = models.EmailField(unique=True, help_text="Work email address")
    position = models.CharField(max_length=100, help_text="Job position or title")

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.id})"


class Task(models.Model):
    """
    Task model representing a task assigned to an employee.
    """
    title = models.CharField(max_length=200, help_text="Title of the task")
    description = models.TextField(blank=True, null=True, help_text="Detailed description of the task")
    completed = models.BooleanField(default=False, help_text="Task completion status")
    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name='tasks',
        help_text="The employee assigned to this task"
    )
    created_at = models.DateTimeField(auto_now_add=True, help_text="Timestamp when task was created")
    updated_at = models.DateTimeField(auto_now=True, help_text="Timestamp when task was last updated")

    def __str__(self):
        return f"{self.title} - {'Done' if self.completed else 'Pending'}"
