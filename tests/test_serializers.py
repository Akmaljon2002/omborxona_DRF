from asosiy.serializers import *
from unittest import TestCase

class TestMahsulotSerializer(TestCase):
    def test_mahsulot(self):
        mahsulot = {
            "id": 1,
		    "nom": "Salyonniy kolbasa",
		    "brend": "Sayohat",
		    "miqdor": 100,
		    "narx": 4000000,
		    "olchov": "kg",
		    "kelgan_sana": "2023-03-30T09:24:48.904083Z",
		    "ombor": 1
        }
        serializer = MahsulotSerializer(data=mahsulot)
        assert serializer.is_valid() == True

class TestClientSerializer(TestCase):
    def test_client(self):
        client = {
            "id": 1,
		    "nom": "Imkon",
		    "manzil": "Farg'ona",
		    "ism": "Akmaljon",
		    "tel": "+998901234576",
		    "qarz": 1000000,
		    "ombor": 1
        }
        serializer = ClientSerializer(data=client)
        assert serializer.is_valid() == True
