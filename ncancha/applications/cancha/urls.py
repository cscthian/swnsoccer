# django
from django.conf.urls import include, url

# local
from . import views


urlpatterns = [
    # urls para la aplicacion cancha
    url(
        r'^$',
        views.IndexListView.as_view(),
        name='index'
    ),
    url(
        r'^campos-deportivos/(?P<flat>[\w\-]+)$',
        views.CampoDeportivoListView.as_view(),
        name='filtro'
    ),
    url(r'^campo-deportvio/(?P<slug>[-\w]+)/$',
        views.CampoDeportivoDetailView.as_view(),
        name='detail'
    ),
]
