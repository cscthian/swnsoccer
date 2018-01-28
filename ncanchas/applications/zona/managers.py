from django.db import models
from django.db.models import Count, Sum
from django.contrib.postgres.search import TrigramSimilarity

class ZoneManager(models.Manager):
    """procedimiento para cancha"""

    def listar_por_distrito(self, distrito):
        """ funcion que devuleve zonas por distrito """

        return self.filter(
            distrito__slug=distrito
        ).order_by('name')

    def count_canchas_by_zone(self):
        """ suma canchas por zona """

        consulta = self.all().values(
            'id',
        ).annotate(
            cantidad=Count("cancha")
        )

        return consulta

    def max_zone_visit(self):
        #zonas mas visitadas
        return self.filter(
            consulta = self.filter(

            )
        )
