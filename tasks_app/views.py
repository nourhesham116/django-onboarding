from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from tasks_app.models import Employee, Task
from tasks_app.serializers import EmployeeSerializer, TaskSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Employee model.
    Handles list, create, retrieve, update, and delete.

    AUTHENTICATION & PERMISSIONS:
    - Read operations (GET): No authentication required (public access)
    - Write operations (POST, PUT, PATCH, DELETE): JWT authentication required

    WHAT THIS MEANS:
    - Anyone can: GET /api/employees/ (list all)
    - Anyone can: GET /api/employees/E001/ (view one)
    - Anyone can: GET /api/employees/?search=John (search)
    - Must login: POST /api/employees/ (create)
    - Must login: PUT /api/employees/E001/ (update)
    - Must login: DELETE /api/employees/E001/ (delete)

    SEARCH FUNCTIONALITY:
    - Endpoint: GET /api/employees/?search=<query>
    - Searches in: first_name, last_name, email, position
    - Example: /api/employees/?search=John
    - Case-insensitive partial matching

    HOW IT WORKS:
    1. JWTAuthentication checks for token (optional for GET)
    2. IsAuthenticatedOrReadOnly allows GET without auth, blocks POST/PUT/DELETE
    3. SearchFilter intercepts requests with ?search= parameter
    4. Creates SQL LIKE queries on specified search_fields
    5. Returns filtered queryset
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'id'  # since Employee has manual PK

    # AUTHENTICATION: Verify JWT tokens (if provided)
    authentication_classes = [JWTAuthentication]

    # PERMISSIONS: Read-only for everyone, write requires authentication
    # - GET requests: Allowed without authentication
    # - POST, PUT, PATCH, DELETE: Requires valid JWT token
    permission_classes = [IsAuthenticatedOrReadOnly]

    # FILTERING: Enable search functionality
    filter_backends = [SearchFilter]  # List of filter classes to apply

    # Fields to search in (supports related field lookups with __)
    search_fields = [
        'first_name',   # Search in first name
        'last_name',    # Search in last name
        'email',        # Search in email
        'position',     # Search in position/job title
    ]
    # SQL generated: WHERE (first_name LIKE '%query%' OR last_name LIKE '%query%' ...)


class TaskViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Task model.
    Handles list, create, retrieve, update, and delete.

    AUTHENTICATION & PERMISSIONS:
    - Read operations (GET): No authentication required (public access)
    - Write operations (POST, PUT, PATCH, DELETE): JWT authentication required

    WHAT THIS MEANS:
    - Anyone can: GET /api/tasks/ (list all)
    - Anyone can: GET /api/tasks/1/ (view one)
    - Anyone can: GET /api/tasks/?completed=true (filter)
    - Must login: POST /api/tasks/ (create)
    - Must login: PUT /api/tasks/1/ (update)
    - Must login: PATCH /api/tasks/1/ (partial update)
    - Must login: DELETE /api/tasks/1/ (delete)

    FILTERING FUNCTIONALITY:
    - Endpoint: GET /api/tasks/?completed=true
    - Endpoint: GET /api/tasks/?completed=false
    - Endpoint: GET /api/tasks/?employee=E001
    - Can combine: /api/tasks/?completed=true&employee=E001

    HOW FILTERING WORKS:
    1. DjangoFilterBackend reads query parameters
    2. Matches them against filterset_fields
    3. Filters queryset with exact matches
    4. Example: ?completed=true → WHERE completed = true

    FILTER OPTIONS:
    - completed: true/false (boolean)
    - employee: employee ID (foreign key)

    SORTING FUNCTIONALITY:
    - Endpoint: GET /api/tasks/?ordering=created_at
    - Endpoint: GET /api/tasks/?ordering=-created_at (descending/newest first)
    - Can combine: GET /api/tasks/?completed=false&ordering=-created_at

    HOW SORTING WORKS:
    1. OrderingFilter reads ?ordering= parameter
    2. Matches against ordering_fields
    3. Adds ORDER BY clause to SQL
    4. Use "-" prefix for descending order

    SORTING OPTIONS:
    - ?ordering=created_at → Oldest first (ascending)
    - ?ordering=-created_at → Newest first (descending) ← Most common
    - ?ordering=title → A-Z by title
    - ?ordering=-title → Z-A by title
    - ?ordering=completed → Pending first (false=0 comes before true=1)
    - ?ordering=-completed → Completed first
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    # AUTHENTICATION: Verify JWT tokens (if provided)
    authentication_classes = [JWTAuthentication]

    # PERMISSIONS: Read-only for everyone, write requires authentication
    # - GET requests: Allowed without authentication
    # - POST, PUT, PATCH, DELETE: Requires valid JWT token
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Enable filtering AND sorting functionality
    filter_backends = [DjangoFilterBackend, OrderingFilter]

    # Fields that can be filtered (exact match)
    filterset_fields = [
        'completed',   # Filter by completion status: ?completed=true or ?completed=false
        'employee',    # Filter by assigned employee: ?employee=E001
    ]

    # Fields that can be used for sorting
    ordering_fields = [
        'created_at',   # Sort by creation date: ?ordering=created_at or ?ordering=-created_at
        'updated_at',   # Sort by last update: ?ordering=updated_at or ?ordering=-updated_at
        'title',        # Sort alphabetically: ?ordering=title or ?ordering=-title
        'completed',    # Sort by status: ?ordering=completed or ?ordering=-completed
    ]

    # Default ordering (if no ?ordering= parameter provided)
    # This ensures consistent results even without explicit sorting
    ordering = ['-created_at']  # Default: Newest tasks first
    # SQL generated: ORDER BY created_at DESC
