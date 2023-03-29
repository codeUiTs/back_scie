from rest_framework.routers import DefaultRouter

from apps.facturaProveedor.api.api import FpViewSet

router = DefaultRouter()

router.register('', FpViewSet, basename="facturas-proveedor")

urlpatterns = router.urls