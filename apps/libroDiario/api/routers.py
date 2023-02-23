from rest_framework.routers import DefaultRouter

from apps.libroDiario.api.api import LdViewSet

router = DefaultRouter()

router.register('', LdViewSet, basename="libroDiario")

urlpatterns = router.urls