from rest_framework.routers import DefaultRouter

from apps.solicitudSuministros.api.api import SsViewSet

router = DefaultRouter()

router.register('', SsViewSet, basename="solicitudSuministros")

urlpatterns = router.urls