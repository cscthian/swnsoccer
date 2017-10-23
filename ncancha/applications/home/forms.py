from django import forms

#local model
from .models import Cancha, Contact

class CanchaForm(forms.ModelForm):

    class Meta:
        model = Cancha
        fields = ('__all__')
        #
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'ejem: monumental de cusco',
                }
            ),
            'reference': forms.Textarea(
                attrs={
                    'placeholder': 'ejem: frente al mercado...',
                }
            ),
            'distrito': forms.TextInput(
                attrs={
                    'placeholder': 'ejem: san sebastian',
                }
            ),
            'maps': forms.TextInput(
                attrs={
                    'placeholder': 'url de google maps',
                }
            ),
            'price': forms.Textarea(
                attrs={
                    'placeholder': 'ejem: dia:20 soles; noche:30 soles',
                }
            ),
            'phone': forms.Textarea(
                attrs={
                    'placeholder': 'ejem: claro:12345678; movistar:12345678',
                }
            ),
            'web': forms.TextInput(
                attrs={
                    'placeholder': 'Url facebook o pagina web',
                }
            ),
        }


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ('__all__')
        #
        widgets = {
            'asunto': forms.TextInput(
                attrs={
                    'placeholder': 'ejem: solicitud de registro',
                }
            ),
            'mensaje': forms.Textarea(
                attrs={
                    'placeholder': 'ejem: podrian por favor ',
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'placeholder': 'ejem: deportstart@gmail.com',
                }
            ),
        }
