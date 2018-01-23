from django.db import models
<<<<<<< HEAD

class CanchaManagers(models.Manager):
    """Procedimientos para modelo Cancha"""

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


=======
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
>>>>>>> d78fc7f6a96a679e8acad816d709fe44920919db
