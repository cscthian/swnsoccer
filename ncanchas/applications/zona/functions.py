#funciones para app zona
#models
from applications.cancha.models import Cancha
from .models import Distrito


def agrupar_distrito_cancha():
    """ devuelve lista de distritos con su numero de canchas y mejor cancha """

    # recuperamos distritos
    distritos = Distrito.objects.all()
    # resultado total
    resultado = []
    # para cada distrito calcuamos num canchas y mejor cancha
    for d in distritos:
        adc = Cancha.objects.agrupar_distrito_cancha(d)
        resultado.append(adc)
    #ordenamos la lista
    resultado = sorted(resultado, key=lambda d:d['count'], reverse=True)
    return resultado
