# django
from django.conf.urls import include, url

# local
from . import views


urlpatterns = [
    # urls para la aplicacion cancha
    url(
        r'^templates/$',
        views.HomeView.as_view(),
        name='home'
    ),
    #muestra mensjae de Confirmacion
    url(
        r'^confirmacion/(?P<flat>[\w\-]+)$',
        views.ConfirmView.as_view(),
        name='confirmacion'
    ),
    #acerca de
    url(
        r'^entretenimiento-pasion-por-el-deporte/$',
        views.NosotrosTemplateView.as_view(),
        name='nosotros'
    ),
    #url para reistrar cancha
    url(
        r'^registrar-mi-campo-deportivo/$',
        views.CanchaCreateView.as_view(),
        name='home_register'
    ),
    #Formulario de Contacto
    url(
        r'^contacta-con-deport-start/$',
        views.ContactCreateView.as_view(),
        name='home_contacto'
    ),
]
