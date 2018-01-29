# -*- coding: utf-8 -*-
from django import forms

#models
from .models import Comentarys, Cancha

class SearchForm(forms.Form):
    """ formulario para buscar  """

    kword = forms.CharField(
        max_length=200,
        required=False,
        widget=forms.TextInput(
            attrs={
                'class':'buscador-search__input',
                'placeholder': 'ingrese nombre, distrito o zona',
                'autofocus':'True'
            }
        )
    )


class ComentarysForm(forms.ModelForm):
    """
    formulario para registrar comentario
    """

    class Meta:
        model = Comentarys
        fields = ('__all__')


class CanchaForm(forms.ModelForm):
    """
    formulario para registrar cancha
    """

    class Meta:
        model = Cancha
        fields = (
            'name',
            'addresse',
            'phone',
            'price_dia',
            'price_noche',
            'description',
            'mapa',
            'number_player',
            'techo',
            'sudaderas',
            'parking',
            'cafetin',
            'sshh',
            'web_url',
            'image',
        )
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class':'form-item__input',
                    'placeholder': 'La bombonera de apelotear...',
                }
            ),
            'addresse': forms.TextInput(
                attrs={
                    'class':'form-item__input',
                    'placeholder': 'Av. los peloteros A-14 ...',
                }
            ),
            'phone': forms.TextInput(
                attrs={
                    'class':'form-item__input',
                    'placeholder': '944147277 - 9123456789',
                }
            ),
            'number_player': forms.NumberInput(
                attrs={
                    'class':'form-item__input',
                    'value': '5',
                }
            ),
            'price_dia': forms.NumberInput(
                attrs={
                    'class':'form-item__input',
                    'placeholder': '30',
                }
            ),
            'price_noche': forms.NumberInput(
                attrs={
                    'class':'form-item__input',
                    'placeholder': '40',
                }
            ),
            'mapa': forms.TextInput(
                attrs={
                    'class':'form-item__input',
                    'placeholder': '**Recuerda que debes ir a la opcion incorporar mapa de google maps',
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class':'form-item__input',
                    'placeholder': 'Ralizamos campeonatos.... al frente de..',
                    'rows': '2',
                }
            ),
            'web_url': forms.URLInput(
                attrs={
                    'class':'form-item__input',
                    'placeholder': 'www.apelotear.com',
                }
            ),
            'techo': forms.CheckboxInput(
                attrs={
                    'class':'form-item-check__input',
                }
            ),
            'parking': forms.CheckboxInput(
                attrs={
                    'class':'form-item-check__input',
                }
            ),
            'sudaderas': forms.CheckboxInput(
                attrs={
                    'class':'form-item-check__input',
                }
            ),
            'cafetin': forms.CheckboxInput(
                attrs={
                    'class':'form-item-check__input',
                }
            ),
            'sshh': forms.CheckboxInput(
                attrs={
                    'class':'form-item-check__input',
                }
            ),
        }
