from django.db import models
from django.db.models import Count
from django.contrib.postgres.search import TrigramSimilarity

class CanchaManager(models.Manager):
    """procedimiento para cancha"""

    def search_cancha(self, name):
        """funcion que busca canchas"""

        #verificamos si nombre tiene mas de 3 digitos
        if len(name) > 3:
            #filtramos por nombre
            consulta1 = self.filter(
                state = True,
                name__trigram_similar=name,
            ).order_by('-points')
            #filtramos por zona
            consulta2 = self.filter(
                state = True,
                zone__name__trigram_similar=name,
            ).order_by('-vists')
            #filtramos por distrito
            consulta3 = self.filter(
                state = True,
                zone__distrito__name__trigram_similar=name,
            ).order_by('-vists')

            resultado = consulta1 | consulta2 | consulta3

            return resultado
        else:
            return self.filter(
                state = True,
                name__icontains=name,
            ).order_by('-vists')[:30]

    def relations_canchas(self, cancha):
        """ funcion que devuleve canchas relaciondas"""
        zones = []
        for z in cancha.zone.all():
            zones.append(z.pk)

        return self.filter(
            state = True,
            zone__in=zones,
        ).distinct()[:6]

    def lista_distritos(self):
        """ agrupa distritos de las zonas """

        consulta = self.filter(
            state = True,
        ).values(
            'zone__distrito__slug',
            'zone__distrito__name'
        ).annotate(
            Count('name')
        )
        return consulta
