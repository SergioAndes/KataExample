from unittest import TestCase

from KataSimple import iteracion1, iteracion2, iteracion3, iteracion4


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

    def test_iteracion2_nNumeros(self):
        self.assertEqual(iteracion2("1,2,4,5"), [4,1], "n numeros")

    # Devolver un arreglo con el número de elementos y el mínimo y el maximo

    def test_iteracion3(self):
        self.assertEqual(iteracion3(""), [0,0,0], "Cadena vacia")

    def test_iteracion3_unNuermo(self):
        self.assertEqual(iteracion3("1"), [1,1,1], "Un numero")

    def test_iteracion3_dosNumeros(self):
        self.assertEqual(iteracion3("1,2"), [2,1,2], "dos numero")

    def test_iteracion3_nNumeros(self):
        self.assertEqual(iteracion3("3,9,5,6"), [4,3,9], "n Numeros")

    # Devolver un arreglo con el número de elementos, el mínimo, el maximo y el promedio

    def test_iteracion4(self):
        self.assertEqual(iteracion4(""), [0,0,0,0], "Cadena vacia")