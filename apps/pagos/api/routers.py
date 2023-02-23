from rest_framework.routers import DefaultRouter

from apps.pagos.api.api import PagoViewSet

router = DefaultRouter()

router.register('', PagoViewSet, basename="pagos")

urlpatterns = router.urls