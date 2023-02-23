from rest_framework.routers import DefaultRouter

from apps.libroMayor.api.api import LmViewSet

router = DefaultRouter()

router.register('', LmViewSet, basename="libroMayor")

urlpatterns = router.urls