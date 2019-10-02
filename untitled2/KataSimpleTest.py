from unittest import TestCase

from KataSimple import iteracion1


class kataSimpleTest(TestCase):
    def test_iteracion1(self):
        self.assertEqual(iteracion1(""), [0], "Cadena vacia")

    def test_iteracion1_unNuermo(self):
        self.assertEqual(iteracion1("1"), [1], "Un numero")

    def test_iteracion1_dosNumeros(self):
        self.assertEqual(iteracion1("1,2"), [2], "Dos numeros")

