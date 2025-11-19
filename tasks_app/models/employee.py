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
    name = models.CharField(max_length=100, help_text="Full name of the employee")
    email = models.EmailField(unique=True, help_text="Work email address")
    position = models.CharField(max_length=100, help_text="Job position or title")

    def __str__(self):
        return f"{self.name} ({self.id})"
