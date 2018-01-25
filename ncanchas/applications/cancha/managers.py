from django.db import models
from django.db.models import Count, Max
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
            ).order_by('-vists')
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

    def agrupar_distrito_cancha(self, distrito):
        """ devuelve un distrito con total de canchas y con cancha mas visitada"""

        consulta = self.filter(
            state=True,
            zone__distrito__pk=distrito.pk
        )

        #cancha mas visitada
        cancha_max = consulta.annotate(
            Max('vists')
        )

        print('cancha_max', cancha_max)

        if consulta.count() > 0:
            resultado = {
                'slug': distrito.slug,
                'name': distrito.name,
                'count': consulta.count(),
                'image': cancha_max[0].image
            }
        else:
            resultado = {
                'slug': distrito.slug,
                'name': distrito.name,
                'count': 0,
                'image': None
            }
        return resultado

    def filter_cancha_by_zone(self, zona):
        return self.filter(
            state=True,
            zone__slug=zona,
        ).order_by(
            '-vists'
        ).order_by(
            'name'
        )

    def search_structure_for_cancha(self, num):
        #buscar por structurure
            if num=='0':
                #con techo
                return self.filter(
                    techo=True,
                    state=False,
                    anulate=False,
                ).order_by('name')[:20]

            elif num=='1':
                 #sin techo
               return self.filter(
                    techo=False,
                    state=False,
                    anulate=False
                ).order_by('name')[:20]

            elif num=='2':
                #con parking
               return self.filter(
                    parking=True,
                    state=False,
                    anulate=False
                ).order_by('name')[:20]

            elif num=='3':
                #t odo
                return self.filter(
                    state=False,
                    anulate=False
                ).order_by('name')[:20]


    def search_structure_for_cancha_distrito(self, num, distrito):
        #buscar por structurure
            if num=='0':
                #con techo
                return self.filter(
                    techo=True,
                    state=False,
                    anulate=False,
                ).order_by('name')[:20]

            elif num=='1':
                 #sin techo
               return self.filter(
                    techo=False,
                    state=False,
                    anulate=False
                ).order_by('name')[:20]

            elif num=='2':
                #con parking
               return self.filter(
                    parking=True,
                    state=False,
                    anulate=False
                ).order_by('name')[:20]

            elif num=='3':
                #t odo
                return self.filter(
                    state=False,
                    anulate=False
                ).order_by('name')[:20]
