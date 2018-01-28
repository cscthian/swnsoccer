# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from . import views

app_name="cancha_app"

urlpatterns = [
    #url para pantalla de inicio
    url(r'^cancha-de-gras/$',
        views.SearchCanchaView.as_view(),
        name='cancha_search'
    ),
    #url para detalle cancha
    url(r'^canchas-en-cusco-peru-en/(?P<slug>[-\w]+)/$',
        views.ZoneFilterCanchaView.as_view(),
        name='filter_by_zone'
    ),
	#url para detalle cancha
    url(r'^detalle/(?P<slug>[-\w]+)/$',
        views.CanchaDetailView.as_view(),
        name='cancha_detalle'
    ),
    #url para pantalla de inicio
    url(r'^registrar-cancha-en-cusco/nuevo/$',
        views.CanchaCreateView.as_view(),
        name='cancha_add'
    ),
    #url para confirmacion de cancha registrada
    url(r'^confirmacion-cancha/(?P<slug>[-\w]+)/$',
        views.MessaggeView.as_view(),
        name='cancha_confimacion'
    ),
    #rul para estructura de una cancah
    url(r'^estructura-cancha/(?P<structure>[-\w]+)/$',
        views.FindStructureView.as_view(),
        name='cancha_structure'
    ),
]

