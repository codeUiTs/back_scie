from django.contrib import admin
from django.urls import include, path, re_path
from django.views.static import serve
from django.conf import settings

from apps.users.views import Login, Logout, UserToken, ManagePassword

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api_authorization/', include('rest_framework.urls')),
    path('login/', Login.as_view(), name = 'login'),
    path('refresh-token/', UserToken.as_view(), name = 'refresh-token'),
    path('logout/', Logout.as_view(), name = 'logout'),
    path('set-password/<int:pk>/', ManagePassword.as_view(), name = 'set-password'),
    path('users/', include('apps.users.api.routers')),
    path('facturas-cliente/', include('apps.facturasCliente.api.routers')),
    path('libroDiario/', include('apps.libroDiario.api.routers')),
    path('libroMayor/', include('apps.libroMayor.api.routers')),
    path('pagos/', include('apps.pagos.api.routers')),
    path('productosVendibles/', include('apps.productosVendibles.api.routers')),
    path('solicitudSuministros/', include('apps.solicitudSuministros.api.routers')),
]

urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    }),
]