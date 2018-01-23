# -*- coding: utf-8 -*-
from django import forms

#models
from .models import Comentarys

class SearchForm(forms.Form):
    """ formulario para buscar  """

    kword = forms.CharField(
        max_length=200,
        required=False,
        widget=forms.TextInput(
            attrs={
                'class':'buscador-search__input',
                'placeholder': 'ingrese nombre, distrito o zona'
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
