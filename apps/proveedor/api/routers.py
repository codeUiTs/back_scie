from rest_framework.routers import DefaultRouter

from apps.proveedor.api.api import ProveedorViewSet

router = DefaultRouter()

router.register('', ProveedorViewSet, basename="proveedor")

urlpatterns = router.urls