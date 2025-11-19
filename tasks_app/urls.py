from rest_framework.routers import DefaultRouter
from tasks_app.views import EmployeeViewSet, TaskViewSet

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet)
router.register(r'tasks', TaskViewSet)

urlpatterns = router.urls
