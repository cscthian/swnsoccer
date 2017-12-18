# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from . import views

app_name="cancha_app"

urlpatterns = [
	#url para pantalla de inicio    
    url(r'^detalle/(?P<pk>\d+)/$',
        views.CanchaDetailView.as_view(),
        name='detalle'
    ),
]
