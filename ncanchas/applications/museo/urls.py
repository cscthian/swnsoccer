# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from . import views

app_name="museo_app"

urlpatterns = [
    #url para museo index
    url(r'^experiencias-deportivas-en-cusco/$',
        views.MuseoView.as_view(),
        name='museo_index'
    ),
    #url para detalle de un album
    url(r'^eventos-deportivos/(?P<slug>[-\w]+)/$',
        views.AlbumDetailView.as_view(),
        name='album_detail'
    ),
]
