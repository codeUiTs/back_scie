from rest_framework.routers import DefaultRouter

from apps.solicitudSuministro.api.api import SsViewSet

router = DefaultRouter()

router.register('', SsViewSet, basename="solicitudSuministro")

urlpatterns = router.urls