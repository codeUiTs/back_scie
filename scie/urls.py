from django.contrib import admin
from django.urls import include, path, re_path
from django.views.static import serve
from django.conf import settings

from apps.user.views import Login, Logout, UserToken, ManagePassword

admin.site.site_header = "Admin panel"
admin.site.index_title = 'Adminstración'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api_authorization/', include('rest_framework.urls')),
    path('login/', Login.as_view(), name = 'login'),
    path('refresh-token/', UserToken.as_view(), name = 'refresh-token'),
    path('logout/', Logout.as_view(), name = 'logout'),
    path('set-password/<int:pk>/', ManagePassword.as_view(), name = 'set-password'),
    path('users/', include('apps.user.api.routers')),
    path('facturas-cliente/', include('apps.facturaCliente.api.routers')),
    path('facturas-proveedor/', include('apps.facturaProveedor.api.routers')),
    path('libroDiario/', include('apps.libroDiario.api.routers')),
    path('libroMayor/', include('apps.libroMayor.api.routers')),
    path('pagos/', include('apps.pago.api.routers')),
    path('producto/', include('apps.producto.api.routers')),
    path('salidaInventario/', include('apps.salidaInventario.api.routers')),
    path('proveedor/', include('apps.proveedor.api.routers')),
    path('planContable/', include('apps.planContable.api.routers')),
    path('solicitudSuministros/', include('apps.solicitudSuministro.api.routers')),
]

urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    }),
]