#django
from django.db import models
from django.contrib.postgres.search import TrigramSimilarity


class CampoManager(models.Manager):
    """ procedimientos para campo deportivo """

    def camps_more_visit(self):
        #devuleve los 50 campos mas visitados
        return self.filter(
            public=True,
        ).order_by(
            '-point',
        )[:50]

    def filter_camps(self, kword, flat):
        #filtramos campos por texto y techo
        if flat=='contecho':
            #con techo
            consulta = self.filter(
                public=True,
                techo=True,
            )
            # nombre
            query1 = consulta.filter(
                name__trigram_similar=kword
            ).order_by('-point')
            #zona
            query2 = consulta.filter(
                addresse__trigram_similar=kword
            ).order_by('-point')
            # referencia
            query3 = consulta.filter(
                reference__trigram_similar=kword
            ).order_by('-point')
            # tag
            query4 = consulta.filter(
                tag__name__trigram_similar=kword
            ).order_by('-point')

            #resultado
            return (query1 | query2 | query3 | query4).distinct()

        elif flat=='sintecho':
            #sin techo
            consulta = self.filter(
                public=True,
                techo=False,
            )
            #por nombre
            # nombre
            query1 = consulta.filter(
                name__trigram_similar=kword
            ).order_by('-point')
            #zona
            query2 = consulta.filter(
                addresse__trigram_similar=kword
            ).order_by('-point')
            # referencia
            query3 = consulta.filter(
                reference__trigram_similar=kword
            ).order_by('-point')
            # tag
            query4 = consulta.filter(
                tag__name__trigram_similar=kword
            ).order_by('-point')

            return (query1 | query2 | query3 | query4)
        else:
            consulta = self.filter(public=True)
            #por nombre
            # nombre
            query1 = consulta.filter(
                name__trigram_similar=kword
            ).order_by('-point')
            #zona
            query2 = consulta.filter(
                addresse__trigram_similar=kword
            ).order_by('-point')
            # referencia
            query3 = consulta.filter(
                reference__trigram_similar=kword
            ).order_by('-point')
            # tag
            query4 = consulta.filter(
                tag__name__trigram_similar=kword
            ).order_by('-point')

            return (query1 | query2 | query3 | query4).distinct()


    def filter_camp_techo(self, flat):

        #con techo
        if flat=='contecho':
            return self.filter(
                public=True,
                techo=True,
            ).order_by('-point')[:50]
        #si techo
        elif flat=='sintecho':
            return self.filter(
                public=True,
                techo=False,
            ).order_by('-point')[:50]
        #todo
        else:
            return self.filter(public=True).order_by('-point')[:100]
