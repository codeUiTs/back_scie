from django.contrib import admin
from django.urls import include, path, re_path
from django.views.static import serve
from django.conf import settings

from apps.user.views import Login, Logout, UserToken, ManagePassword

admin.site.site_header = "Admin panel"
admin.site.index_title = 'Adminstración'

urlpatterns = [
    path('', admin.site.urls),
    path('api_authorization/', include('rest_framework.urls')),
    path('api/login/', Login.as_view(), name = 'login'),
    path('api/refresh-token/', UserToken.as_view(), name = 'refresh-token'),
    path('api/logout/', Logout.as_view(), name = 'logout'),
    path('api/set-password/<int:pk>/', ManagePassword.as_view(), name = 'set-password'),
    path('api/users/', include('apps.user.api.routers')),
    path('api/facturas-cliente/', include('apps.facturaCliente.api.routers')),
    path('api/libroDiario/', include('apps.libroDiario.api.routers')),
    path('api/libroMayor/', include('apps.libroMayor.api.routers')),
    path('api/pagos/', include('apps.pago.api.routers')),
    path('api/producto/', include('apps.producto.api.routers')),
    path('api/salidaInventario/', include('apps.salidaInventario.api.routers')),
    path('api/proveedor/', include('apps.proveedor.api.routers')),
    path('api/planContable/', include('apps.planContable.api.routers')),
    path('api/solicitudSuministros/', include('apps.solicitudSuministro.api.routers')),
]

urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    }),
]