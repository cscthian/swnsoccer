# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from . import views

app_name="zone_app"

urlpatterns = [
    #url para listar distritos
    url(
        r'^cancha-de-gras-en-distritos-de-cusco/$',
        views.DistritoListView.as_view(),
        name='lista_distritos'
    ),
	#url para listar zonas por ditrito
    url(
        r'^cancha-de-gras-en-el-distrito/(?P<slug>[-\w]+)/$',
        views.ZoneByDistritoView.as_view(),
        name='zona_by_distrito'
    ),
]
