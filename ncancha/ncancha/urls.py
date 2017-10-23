from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView


urlpatterns = [
    # urls para la aplicacion home
    url(r'^admin/', admin.site.urls),
    #urs para cancha
    url(r'^', include('applications.cancha.urls', namespace="cancha_app")),
    #urls para home
    url(r'^', include('applications.home.urls', namespace="home_app")),
    # # PYTHON SOCIAL AUTH
    # url('', include('social.apps.django_app.urls', namespace='social')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
