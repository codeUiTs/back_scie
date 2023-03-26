from rest_framework.routers import DefaultRouter

from apps.producto.api.api import ProductoViewSet

router = DefaultRouter()

router.register('', ProductoViewSet, basename="producto")

urlpatterns = router.urls