from unittest import TestCase

from KataSimple import iteracion1, iteracion2


class KataSimpleTest(TestCase):

    # Devolver un arreglo con el número de elementos

    def test_iteracion1(self):
        self.assertEqual(iteracion1(""), [0], "Cadena vacia")

    def test_iteracion1_unNuermo(self):
        self.assertEqual(iteracion1("1"), [1], "Un numero")

    def test_iteracion1_dosNumeros(self):
        self.assertEqual(iteracion1("1,2"), [2], "Dos numeros")

    def test_iteracion1_nNumeros(self):
        self.assertEqual(iteracion1("1,2,4,5"), [4], "N Numeros")

    # Devolver un arreglo con el número de elementos y el mínimo

    def test_iteracion2(self):
        self.assertEqual(iteracion2(""), [0,0], "Cadena vacia")

    def test_iteracion2_unNuermo(self):
        self.assertEqual(iteracion2("1"), [1,1], "Un numero")

    def test_iteracion2_dosNumeros(self):
        self.assertEqual(iteracion2("1,2"), [2,1], "dos numeros")
