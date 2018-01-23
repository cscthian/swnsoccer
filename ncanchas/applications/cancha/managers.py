from django.db import models

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


