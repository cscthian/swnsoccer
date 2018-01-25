#dango templates
from django import template
#
register = template.Library()

@register.filter(name='class_change')
def class_change(value):
    array = value.split('<iframe')
    print('arrgelo split', array)
    valor = '<iframe id="cancha-mapa__map" '+array[1]
    return valor
