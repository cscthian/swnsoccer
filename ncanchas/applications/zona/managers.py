from django.db import models
from django.contrib.postgres.search import TrigramSimilarity

class ZoneManager(models.Manager):
    """procedimiento para cancha"""

    def listar_por_distrito(self, distrito):
        """ funcion que devuleve zonas por distrito """

        return self.filter(
            distrito__slug=distrito
        ).order_by('name')
