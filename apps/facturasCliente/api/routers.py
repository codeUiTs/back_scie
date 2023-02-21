from rest_framework.routers import DefaultRouter

from apps.facturasCliente.api.api import FcViewSet

router = DefaultRouter()

router.register('', FcViewSet, basename="facturas-cliente")

urlpatterns = router.urls