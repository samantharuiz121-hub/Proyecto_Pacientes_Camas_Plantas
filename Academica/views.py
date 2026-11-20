from django.shortcuts import render, get_object_or_404
from Academica.models import Paciente, Cama, Planta

# Create your views here.

## Pacientes

def listaPacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, 'pacientes/listado_pacientes.html',
                 {'pacientes': pacientes})


def detallePaciente(request, id):
    paciente = get_object_or_404(Paciente, cedula_pac=id)
    camas = Cama.objects.filter(cedula_paciente=paciente).select_related('numero_planta')
    return render(request, 'pacientes/detalle_paciente.html',
                  {'paciente': paciente, 'camas': camas})

## Plantas

def listaPlantas(request):
    plantas = Planta.objects.all()
    return render(request, 'plantas/listado_plantas.html',
                  {'plantas': plantas})


def detallePlanta(request, id):
    planta = get_object_or_404(Planta, numero_pln=id)
    camas = Cama.objects.filter(numero_planta=planta).select_related('cedula_paciente')
    return render(request, 'plantas/detalle_planta.html',
                  {'planta': planta, 'camas': camas})

## Camas

def listaCamas(request):
    camas = Cama.objects.select_related('numero_planta', 'cedula_paciente')
    return render(request, 'camas/listado_camas.html',
                  {'camas': camas})


def detalleCama(request, id):
    cama = get_object_or_404(
        Cama.objects.select_related('numero_planta', 'cedula_paciente'),
        codigo_cam=id
    )
    return render(request, 'camas/detalle_cama.html', {'cama': cama})
