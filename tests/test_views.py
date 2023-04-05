from asosiy.views import *
from asosiy.models import Client, Mahsulot
from unittest import TestCase
from rest_framework.test import APIClient


class TestClientViewSet(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()

    # def test__all_clients_view(self):
    #     natija = self.client.get('/clientlar/')
    #     # assert natija.status_code == 200
    #     print(natija.data)
    #     assert len(natija.data) == Client.objects.count()
        # if len(natija.data) != 0:
        #     assert natija.data[0]['ism'] == Client.objects.first().ism
        #     assert natija.data[0]['nom'] == Client.objects.first().nom

    # def test_client(self):
    #     natija = self.client.get('/clientlar/1/')
    #     assert natija.data['ism'] == Client.objects.get(id=1).ism

    def test_client_qoshish(self):
        mijoz = {
		    "nom": "Asl baraka",
		    "manzil": "Farg'ona",
		    "ism": "Akmaljon",
		    "tel": "+998901234576",
		    "qarz": 2000000,
		    "ombor": 1
        }
        natija = self.client.post('/clientlar/', data=mijoz)
        assert natija.status_code == 201
    #

class TestMahsulotViewSet(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()

    def test_mahsulot(self):
        natija = self.client.get('/mahsulotlar/')
        # assert natija.status_code == 200
        assert len(natija.data) == Mahsulot.objects.count()
        # if len(natija.data) != 0:
        #     assert natija.data[0]['nom'] == Mahsulot.objects.first().nom

    def test_mahsulot_qoshish(self):
        mahsulot = {
            "nom": "Kapchonni",
            "brend": "Davr",
            "miqdor": 100,
            "narx": 2000000,
            "olchov": "kg",
            "kelgan_sana": "2023-03-30T09:24:48.904083Z",
            "ombor": 1
        }
        natija = self.client.post('/mahsulotlar/', data=mahsulot)
        assert natija.status_code == 202