from django.db import models
from tasks_app.models.employee import Employee

class Task(models.Model):
    """
    Task model representing a task assigned to an employee.
    """
    title = models.CharField(max_length=200, help_text="Title of the task")
    description = models.TextField(blank=True, help_text="Detailed description of the task")
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
