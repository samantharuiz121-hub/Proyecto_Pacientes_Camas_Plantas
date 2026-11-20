from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Academica.views import (
    listaPacientes, detallePaciente,
    listaCamas, detalleCama,
    listaPlantas, detallePlanta
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', listaPacientes, name='inicio'),
    path('pacientes/', listaPacientes, name='listado_pacientes'),
    path('pacientes/detalle/<str:id>/', detallePaciente, name='detallePaciente'),
    path('camas/', listaCamas, name='listado_camas'),
    path('camas/detalle/<int:id>/', detalleCama, name='detalleCama'),
    path('plantas/', listaPlantas, name='listado_plantas'),
    path('plantas/detalle/<int:id>/', detallePlanta, name='detallePlanta'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
