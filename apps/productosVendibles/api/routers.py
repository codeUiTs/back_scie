from rest_framework.routers import DefaultRouter

from apps.productosVendibles.api.api import PvViewSet

router = DefaultRouter()

router.register('', PvViewSet, basename="productosVendibles")

urlpatterns = router.urls