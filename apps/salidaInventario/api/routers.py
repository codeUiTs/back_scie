from rest_framework.routers import DefaultRouter

from apps.salidaInventario.api.api import SalidaInventarioViewSet

router = DefaultRouter()

router.register('', SalidaInventarioViewSet, basename="salidaInventario")

urlpatterns = router.urls