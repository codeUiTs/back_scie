from rest_framework.routers import DefaultRouter

from apps.productoVendible.api.api import PvViewSet

router = DefaultRouter()

router.register('', PvViewSet, basename="productoVendible")

urlpatterns = router.urls