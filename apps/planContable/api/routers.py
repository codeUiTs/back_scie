from rest_framework.routers import DefaultRouter

from apps.planContable.api.api import PlanContableViewSet

router = DefaultRouter()

router.register('', PlanContableViewSet, basename="planContable")

urlpatterns = router.urls