from django.urls import reverse
from django.test import TestCase
from django.urls.exceptions import NoReverseMatch

from musiques.models import Morceau, Artiste


class MorceauTestCase(TestCase):
    def setUp(self):
        Morceau.objects.create(titre='musique1', artiste='artise1')
        Morceau.objects.create(titre='musique2', artiste='artise2')
        Morceau.objects.create(titre='musique3', artiste='artise3')
        Morceau.objects.create(titre='musique4')
        Artiste.objects.create(nom='artiste1')
        Artiste.objects.create(nom='artiste2')

    def test_morceau_url_name(self):
        try:
            url = reverse('musiques:morceau-detail', args=[1])
        except NoReverseMatch:
            assert False


    def test_morceau_url(self):
        morceau = Morceau.objects.get(titre='musique1')
        url = reverse('musiques:morceau-detail', args=[morceau.pk])
        response = self.client.get(url)
        assert response.status_code == 200

    def test_artiste_url_name(self):
        try:
            url = reverse('musiques:artiste-detail',args=[0])
        except NoReverseMatch:
            assert False
    
    def test_artiste_url(self):
        artiste = Artiste.objects.get(nom='artiste1')
        url = reverse('musiques:artiste-detail', args=[artiste.pk])
        response = self.client.get(url)
        assert response.status_code == 200

    # def test_morceau_existe_pas(self):
    #     try:
    #         morceau = Morceau.objects.get(titre='musique5')
    #         url = reverse('musiques:morceau-detail', args=[morceau.pk])
    #         response = self.client.get(url)
    #         assert False
    #     except PageNotFound:
    #         assert True
    
    # def test_Musique_sans_artiste(self):
        
    #     morceau = Morceau.objects.get(titre='musique4')
    #     assert morceau.artiste ==null

    # // bd
    # // ajout
    # // url
