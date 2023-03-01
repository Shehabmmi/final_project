from rest_framework import routers
from .views import AssignmentViewSet


router = routers.SimpleRouter()

router.register(r'assignments', AssignmentViewSet)

urlpatterns = router.urls



